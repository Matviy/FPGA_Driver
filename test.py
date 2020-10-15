class Register:
   def __init__(self, name, offset, size, endian, signed):
      self.name   = name
      self.offset = offset
      self.size   = size
      self.endian = endian
      self.signed = signed

registers = {
	"CLOCK_LATCH_FREQ": Register("CLOCK_LATCH_FREQ",0x140,  4, "little", False),
	"LED_FLASH_RATE":	Register("LED_FLASH_RATE",  0x144,  4, "little", False),
	"FAN_1_SPEED": 		Register("FAN_1_SPEED",     0x106,  4, "little", False),
	"FAN_2_SPEED": 		Register("FAN_2_SPEED",     0x10A,  4, "little", False),
	"SCRATCH": 		    Register("SCRATCH",         0x130,  4, "little", False)
}


with open("char_device", "r+b") as file_fpga:

   # Test byte sequences
   write_tests = [
	[0xAA, 0xBB, 0xCC, 0xDD],
	[0x11, 0x22]
   ]

   print("Write Tests:")
   for test in write_tests:
      file_fpga.seek(registers["SCRATCH"].offset)
      file_fpga.write(bytearray(test))
      file_fpga.seek(registers["SCRATCH"].offset)
      read_bytes = file_fpga.read(registers["SCRATCH"].size)
      print([hex(c) for c in read_bytes])

   # Register read test
   print("\nRead Tests:")
   for reg in registers.values():

      file_fpga.seek(reg.offset)
      read_bytes = file_fpga.read(reg.size)

      val = int.from_bytes(read_bytes, reg.endian, signed=reg.signed)
      print(f"Register: {reg.name} Value: {val}")
