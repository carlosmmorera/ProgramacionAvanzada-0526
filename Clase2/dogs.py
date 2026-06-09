import requests
from PIL import Image
from io import BytesIO


class DogAPI:

    def __init__(self):
        self.__base_url = "https://dog.ceo/api/breeds"
        self.__response = None

    @property
    def base_url(self):
        return self.__base_url
    
    @property
    def response(self):
        return self.__response
    
    @response.setter
    def response(self,value):
        self.__response = value

    @base_url.setter
    def base_url(self,value):
        self.__base_url = value

    

    def get_random_dog_image(self):
        url = self.base_url + "/image/random"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["status"] == "success":
                return data["message"]
            else:
                print("Failed to fetch dog image.")
                return None
        except requests.RequestException as e:
            print(f"Error fetching dog image: {e}")
            return None


    def display_image_from_url(self, image_url):
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            img.show()
        except requests.RequestException as e:
            print(f"Error fetching image: {e}")

    #Obtiene varias imagenes de perros, el numero de imagenes se le pasa como parametro. Devuelve una lsita con las urls de las imagenes
    def get_random_dog_images(self,number_of_images):
            url = self.base_url + "/image/random/"+number_of_images
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                if data["status"] == "success":
                    return data["message"]
                else:
                    print("Failed to fetch dog image.")
                    return None
            except requests.RequestException as e:
                print(f"Error fetching dog image: {e}")
                return None
    

    #Muestra varias imagenes de perros, se le pasan las urls en una lista
    def display_images_from_urls(self, image_urls):
        for image_url in image_urls:
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content))
                img.show()
            except requests.RequestException as e:
                print(f"Error fetching image: {e}")









    #No se ha llegado a hacer
    def get_all_dogs_breeds():
        url = "https://dog.ceo/api/breeds/list/all"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["status"] == "success":
                return data["message"]
            else:
                print("Failed to fetch dog breeds.")
                return None
        except requests.RequestException as e:
            print(f"Error fetching dog breeds: {e}")
            return None
        
def main():
    print("Dog CEO API Test\n")
    dog_api = DogAPI()
    image_url = dog_api.get_random_dog_image()
    if image_url:
        print(f"Random Dog Image: {image_url}\n")
        dog_api.display_image_from_url(image_url)

    images_urls = dog_api.get_random_dog_images("3")
    if images_urls:
        print(f"Random Dog Images: {images_urls}\n")
        dog_api.display_images_from_urls(images_urls)
    

if __name__ == "__main__":
    main()
