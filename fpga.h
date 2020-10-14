#define FPGA_VENDOR 0x9999
#define FPGA_DEVICE 0x0001

#define DRIVER_NAME "Fpga Driver"

#define MAJNUM 99
#define DEVICE_COUNT 1

#define BAR_0 0

struct fpga {
	struct pci_dev* pci_dev;
	void* pci_regs;
	struct cdev char_dev;
	unsigned int offset;
};