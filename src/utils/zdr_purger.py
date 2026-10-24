# 2-Pass ZDR Memory Purger (0xAA -> 0x00)
import gc

class ZDRPurger:
    @staticmethod
    def purge(buffer: bytearray = None) -> bool:
        if buffer is not None and isinstance(buffer, bytearray):
            for i in range(len(buffer)):
                buffer[i] = 0xAA
            for i in range(len(buffer)):
                buffer[i] = 0x00
        gc.collect()
        return True
