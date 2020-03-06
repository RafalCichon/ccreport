import io
import zipfile


class ZipUtils:
    @staticmethod
    def read_entry_content(full_zip_content, entry_path):
        with zipfile.ZipFile(io.BytesIO(full_zip_content)) as zip_file:
            for name in zip_file.namelist():
                if not name == entry_path:
                    continue
                with zip_file.open(name) as zip_entry:
                    return zip_entry.read()
        return None
