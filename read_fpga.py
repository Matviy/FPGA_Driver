class Register:
   def __init__(self, name, offset, size, endian, signed):
      self.name   = name
      self.offset = offset
      self.size   = size
      self.endian = endian
      self.signed = signed

registers = [
	Register("CLOCK_LATCH_FREQ", 0x100,  4, "little", False),
	Register("LED_FLASH_RATE",   0x104,  2, "little", False),
	Register("FAN_1_SPEED",      0x106,  4, "little", False),
	Register("FAN_2_SPEED",      0x10A,  4, "little", False),
]

with open("char_device", "rb") as file_fpga:

    for reg in registers:
       file_fpga.seek(reg.offset)
       read_bytes = file_fpga.read(reg.size)
       val = int.from_bytes(read_bytes, reg.endian, signed=reg.signed)
       print(f"Register: {reg.name} Value: {val}")
