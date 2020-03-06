class BytesUtils:
    @staticmethod
    def join_chunks(chunks):
        joined_chunks = bytes(0)
        for c in chunks:
            joined_chunks += c
        return joined_chunks
