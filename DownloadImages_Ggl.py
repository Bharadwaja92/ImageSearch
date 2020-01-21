from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

def download_images(query, num_images):
    arguments = {"keywords": query, "format": "jpg", "limit": num_images, "print_urls": True,
                 "size": "medium", "aspect_ratio": "panoramic"}
    try:
        response.download(arguments=arguments)
    except FileNotFoundError:
        arguments = {"keywords": query, "format": "jpg","limit": 4, "print_urls": True, "size": "medium"}
        try:
            response.download(arguments)
        except:
            pass


search_query = 'Popeye'
num_images = 10
download_images(search_query, num_images)

print('Done')