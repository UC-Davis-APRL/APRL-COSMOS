from openc3.conversions.conversion import Conversion
# Using tlm() requires the following:
# from openc3.api.tlm_api import tlm

# Custom conversion class
# See https://docs.openc3.com/docs/configuration/telemetry#read_conversion


class LcSumConversion(Conversion):
    def __init__(self):
        super().__init__()
        # Should be one of 'INT', 'UINT', 'FLOAT', 'STRING', 'BLOCK'
        self.converted_type = 'FLOAT'
        # Size of the converted type in bits
        # Use 0 for 'STRING' or 'BLOCK' where the size can be variable
        self.converted_bit_size = 64

    # @param value [Object] Value based on the item definition. This could be
    #   a string, integer, float, or array of values.
    # @param packet [Packet] The packet object where the conversion is defined
    # @param buffer [String] The raw packet buffer
    def call(self, value, packet, buffer):
        # Read values from the packet and do a conversion
        # Used for DERIVED items that don't have a value

        l1 = packet.read("LOAD1")
        l2 = packet.read("LOAD2")
        l3 = packet.read("LOAD3")
        l4 = packet.read("LOAD4")

        n = min(len(l1), len(l2), len(l3), len(l4))
        return [l1[i] + l2[i] + l3[i] + l4[i] for i in range(n)]