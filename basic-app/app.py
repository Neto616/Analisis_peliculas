# Express
from shiny import reactive, render
from shiny.express import input, render, ui
import requests

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZmQ4Y2QzZjkxMjRkMWE1NGM3YjY5YmRiYThjMDY5YiIsIm5iZiI6MTczMzQ5NTYwOS43MTI5OTk4LCJzdWIiOiI2NzUzMGIzOTg3MWE0MmM5YzI0NTM3OGQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Knqg2KvakNDO-sb3feSiwc-Cyc-NPhCbOUTz9wF2xao"
}

ui.page_opts(title="Analizis de peliculas")

with ui.sidebar():
    ui.input_text("peliculasInput", "Pelicula: ")

response = (requests.get(url, headers=headers)).json()['results']
# counter = 0
# card = []
# for y, x in enumerate(response):
#     card_id = f"card_{y}"
#     with(ui.card(full_screen=True, id=card_id)):
#         @render.ui
#         def result():
#             print(x['original_title'])
#             return f"Titulo {y}: {x['original_title']}"
              
with ui.card(full_screen=True):
    @render.ui
    def result():
#        print(response)
        if len(input.peliculasInput()) == 0:
            cards = []
            for x in response:
                print(x['title'])
                cards.append(ui.div(
                    ui.h3(f"{x['title']}"), 
                    ui.p(f"{str(x['overview'])}")))
            #     data += f"||Pelicula {counter}: {x['title']}"
            #     counter += 1
            return cards
        
        return f"Pelicula a buscar: '{input.peliculasInput()}'"
    
