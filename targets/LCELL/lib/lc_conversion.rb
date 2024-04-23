# encoding: ascii-8bit
require 'openc3/conversions/conversion'

module OpenC3

  # Custom conversion class for converting loadcell ADC counts to force
  # See https://openc3.com/docs/v5/telemetry#read_conversion
  
  class LcConversion < Conversion
    def initialize(range_kg, offset_kg, scaleFactor_x)
      super()
      # Should be one of :INT, :UINT, :FLOAT, :STRING, :BLOCK
      @converted_type = :FLOAT
      # Size of the converted type in bits
      # Use 0 for :STRING or :BLOCK where the size can be variable
      @converted_bit_size = 64
      # Multiplier converting voltages to output values
      @range_kg = range_kg.to_f
      @offset_kg = offset_kg.to_f
      @scaleFactor_x = scaleFactor_x.to_f
    end

    # @param value [Object] Value based on the item definition. This could be
    #   a string, integer, float, or array of values.
    # @param packet [Packet] The packet object where the conversion is defined
    # @param buffer [String] The raw packet buffer
    def call(value, packet, buffer)
      
      # Perform conversion logic directly on value
      # Used when conversion is applied to a regular (not DERIVED) item
      # NOTE: You can also use packet.read("ITEM") to get additional values
      # return ((value * (5.0 / 8388608)) - 0.00) / 1.280 * @sensor_range

      # Constants
      adc_reference_voltage = 5.0  # The reference voltage of ADC
      pga_gain = 128.0             # The PGA gain
      excitation_voltage = 5.0     # Load cell excitation voltage
      sensitivity_mvv = 2.0

      # Calculating full scale output voltage of the load cell in mV
      full_scale_output_mV = excitation_voltage * sensitivity_mvv * @scaleFactor_x

      # Perform sign extension from 24-bit to 32-bit if necessary
      if value & 0x00800000 != 0  # Check if the 24th bit is set (negative number)
        value |= 0xFF000000  # Extend the sign to the 32-bit integer
      end

      # Convert ADC count to voltage considering the PGA gain
      # Adjusting the calculation to correctly scale bipolar ADC output from -8388608 to +8388607
      voltage_measured = (value.to_f / 8388608.0) * (adc_reference_voltage / pga_gain)

      # Convert voltage to millivolts
      voltage_in_millivolts = voltage_measured * 1000.0

      # Calculate force based on the voltage and the full scale output
      # Formula matches expected format
      force = (voltage_in_millivolts / full_scale_output_mV) * @range_kg + @offset_kg

      return force
    end
  end
end
