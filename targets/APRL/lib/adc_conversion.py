from openc3.conversions.conversion import Conversion
# Using tlm() requires the following:
# from openc3.api.tlm_api import tlm

# Custom conversion class
# See https://docs.openc3.com/docs/configuration/telemetry#read_conversion


class AdcConversion(Conversion):
    def __init__(self, range_psi, offset_psi):
        super().__init__()
        # Should be one of 'INT', 'UINT', 'FLOAT', 'STRING', 'BLOCK'
        self.converted_type = 'FLOAT'
        # Size of the converted type in bits
        # Use 0 for 'STRING' or 'BLOCK' where the size can be variable
        self.converted_bit_size = 64
        # Multiplier converting voltages to output values
        self.range_psi = float(range_psi)
        self.offset_psi = float(offset_psi)

    def _convert_one(self, value):

        # Perform sign extension from 24-bit to 32-bit if necessary
        if (value & 0x00800000) != 0:  # Check if the 24th bit is set (negative number)
            value |= 0xFF000000  # Extend the sign to the 32-bit integer
        
        return ((value * (5.0 / 8388608)) - 0.48) / 1.92 * self.range_psi + self.offset_psi

    # @param value [Object] Value based on the item definition. This could be
    #   a string, integer, float, or array of values.
    # @param packet [Packet] The packet object where the conversion is defined
    # @param buffer [String] The raw packet buffer
    def call(self, value, packet, buffer):

        # value is a list for ARRAY_ITEMs; support both list and scalar
        if isinstance(value, (list, tuple)):
            return [self._convert_one(x) for x in value]
        return self._convert_one(value)
