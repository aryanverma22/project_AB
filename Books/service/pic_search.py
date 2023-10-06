import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
def get_thumbnails(search_term, count = 1):
    thumbnails = []

    try:
        url = rf'https://www.google.no/search?q={search_term}&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&safe=active&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'

        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')


        for raw_img in soup.find_all('img'):
            link = raw_img.get('src')
            if link and link.startswith("https://"):
                thumbnails.append(link)

                if len(thumbnails) >= count:
                    return thumbnails
                pass
            pass

        return thumbnails
    except Exception as e:
        sError = f"""Error: {e}
        search_term: {search_term}
        """
        print(sError)
        return thumbnails
    pass


def get_book_pic(book, author):
    search_query= f"{book}+{author}"
    image_link= get_thumbnails(search_query)
    return image_link


print(get_book_pic('ikigai','Hector garcia'))