from math import ceil


class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.build_matrix(pages)

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.MAX_PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for idx_page, list_photo_slots in enumerate(self.photos):
            if len(list_photo_slots) < PhotoAlbum.MAX_PHOTOS_PER_PAGE:
                list_photo_slots.append(label)
                return f"{label} photo added successfully on page {idx_page + 1} slot {len(list_photo_slots)}."
        return "No more free slots"

    def display(self):
        delimiter = '-' * 11
        result = delimiter + '\n'
        for page in self.photos:
            result += ' '.join(['[]' for slot in page]) + '\n'
            result += delimiter + '\n'
        return result.strip()

    def build_matrix(self, pages):
        return [[] for _ in range(pages)]


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
