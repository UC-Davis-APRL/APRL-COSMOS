# encoding: ascii-8bit
require 'openc3/conversions/conversion'

module OpenC3
  # Custom conversion class
  # See https://openc3.com/docs/v5/telemetry#read_conversion
  class LcConversion < Conversion
    def initialize(range_kg, offset_kg, sensitivity_mvv)
      super()
      # Should be one of :INT, :UINT, :FLOAT, :STRING, :BLOCK
      @converted_type = :FLOAT
      # Size of the converted type in bits
      # Use 0 for :STRING or :BLOCK where the size can be variable
      @converted_bit_size = 64
      # Multiplier converting voltages to output values
      @range_kg = range_kg.to_f
      @offset_kg = offset_kg.to_f
      @sensitivity_mvv = sensitivity_mvv.to_f
    end

    # @param value [Object] Value based on the item definition. This could be
    #   a string, integer, float, or array of values.
    # @param packet [Packet] The packet object where the conversion is defined
    # @param buffer [String] The raw packet buffer
    def call(value, packet, buffer)
      # Read values from the packet and do a conversion
      # Used for DERIVED items that don't have a value
      # item1 = packet.read("ITEM1") # returns CONVERTED value (default)
      # item2 = packet.read("ITEM2", :RAW) # returns RAW value
      # return (item1 + item2) / 2
      #
      # Perform conversion logic directly on value
      # Used when conversion is applied to a regular (not DERIVED) item
      # NOTE: You can also use packet.read("ITEM") to get additional values
      # return ((value * (5.0 / 8388608)) - 0.00) / 1.280 * @sensor_range

      # Constants
      adc_reference_voltage = 5.0  # The reference voltage of ADC
      pga_gain = 128.0             # The PGA gain
      excitation_voltage = 5.0     # Load cell excitation voltage

      # Calculating full scale output voltage of the load cell in mV
      full_scale_output_mV = excitation_voltage * @sensitivity_mvv

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
      force = (voltage_in_millivolts / full_scale_output_mV) * @range_kg - @offset_kg

      return force
    end
  end
end
