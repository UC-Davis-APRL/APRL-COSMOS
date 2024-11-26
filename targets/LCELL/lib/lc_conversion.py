from openc3.conversions.conversion import Conversion
# Using tlm() requires the following:
# from openc3.api.tlm_api import tlm

# Custom conversion class
# See https://docs.openc3.com/docs/configuration/telemetry#read_conversion


class LcConversion(Conversion):
    def __init__(self, range_kg, offset_kg, scaleFactor_x):
        super().__init__()
        # Should be one of 'INT', 'UINT', 'FLOAT', 'STRING', 'BLOCK'
        self.converted_type = 'FLOAT'
        # Size of the converted type in bits
        # Use 0 for 'STRING' or 'BLOCK' where the size can be variable
        self.converted_bit_size = 64
        # Multiplier converting voltages to output values
        self.range_kg = float(range_kg)
        self.offset_kg = float(offset_kg)
        self.scaleFactor_x = float(scaleFactor_x)

    # @param value [Object] Value based on the item definition. This could be
    #   a string, integer, float, or array of values.
    # @param packet [Packet] The packet object where the conversion is defined
    # @param buffer [String] The raw packet buffer
    def call(self, value, packet, buffer):

        # Perform conversion logic directly on value
        # Used when conversion is applied to a regular (not DERIVED) item
        # NOTE: You can also use packet.read("ITEM") to get additional values

        # Constants
        adc_reference_voltage = 5.0  # The reference voltage of ADC
        pga_gain = 128.0             # The PGA gain
        excitation_voltage = 5.0     # Load cell excitation voltage
        sensitivity_mvv = 2.0

        # Calculating full scale output voltage of the load cell in mV
        full_scale_output_mV = excitation_voltage * sensitivity_mvv * self.scaleFactor_x

        # Perform sign extension from 24-bit to 32-bit if necessary
        if (value & 0x00800000) != 0:  # Check if the 24th bit is set (negative number)
            value |= 0xFF000000  # Extend the sign to the 32-bit integer
        
        # Convert ADC count to voltage considering the PGA gain
        # Adjusting the calculation to correctly scale bipolar ADC output from -8388608 to +8388607
        voltage_measured = (float(value) / 8388608.0) * (adc_reference_voltage / pga_gain)

        # Convert voltage to millivolts
        voltage_in_millivolts = voltage_measured * 1000.0

        # Calculate force based on the voltage and the full scale output
        # Formula matches expected format
        force = (voltage_in_millivolts / full_scale_output_mV) * self.range_kg + self.offset_kg

        return force
