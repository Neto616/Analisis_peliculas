# Express
from shiny import reactive, render
from shiny.express import input, render, ui
from funciones import *
#response = (requests.get(url, headers)).json()['results']    
ui.page_opts(title="Analizis de peliculas")

with ui.sidebar():
    ui.input_text("peliculasInput", "Pelicula: ")
    ui.input_action_button("buscar", "Buscar pelicula")
    
    # generos_response = peticion_api("https://api.themoviedb.org/3/genre/movie/list?language=en", {
    # "accept": "application/json",
    # "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZmQ4Y2QzZjkxMjRkMWE1NGM3YjY5YmRiYThjMDY5YiIsIm5iZiI6MTczMzQ5NTYwOS43MTI5OTk4LCJzdWIiOiI2NzUzMGIzOTg3MWE0MmM5YzI0NTM3OGQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Knqg2KvakNDO-sb3feSiwc-Cyc-NPhCbOUTz9wF2xao"
    # })['genres']
    
    # ui.input_checkbox_group("generos", "Generos",
    #                         {generos_response["name"]: generos_response["name"] for generos_response in generos_response})
    # @render.text()
    # def genero():
    #     print(input.generos())

with ui.card(full_screen= True):
    @render.ui
    def result():
        response = peticion_api("https://api.themoviedb.org/3/movie/912649/reviews?language=en-US&page=1", {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZmQ4Y2QzZjkxMjRkMWE1NGM3YjY5YmRiYThjMDY5YiIsIm5iZiI6MTczMzQ5NTYwOS43MTI5OTk4LCJzdWIiOiI2NzUzMGIzOTg3MWE0MmM5YzI0NTM3OGQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Knqg2KvakNDO-sb3feSiwc-Cyc-NPhCbOUTz9wF2xao"
         })["results"]
        
        """
            response tiene los siguientes datos:
            'author': Nombre de la persona que escribio la reseña.
            'author_details': Detalles de la persona que escribio la reseña
            'content': La reseña
            'created_at': fecha de creación de la reseña
            'id': id de la reseña
            'updated_at': fecha de actualizacion de la reseña (supongo)
            'url': link de la reseña
        """
        jsonFormat(response)
# Esto sirve
# with ui.card(full_screen=True):
#     @render.ui
#     def result():
#         # # Activar cuando se quiera tener respuesta de la API
#         # url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
#         # headers = {
#         #     "accept": "application/json",
#         #     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiZmQ4Y2QzZjkxMjRkMWE1NGM3YjY5YmRiYThjMDY5YiIsIm5iZiI6MTczMzQ5NTYwOS43MTI5OTk4LCJzdWIiOiI2NzUzMGIzOTg3MWE0MmM5YzI0NTM3OGQiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.Knqg2KvakNDO-sb3feSiwc-Cyc-NPhCbOUTz9wF2xao"
#         # }
#         # response = peticion_api(url, headers)["results"]
        
#         response = ({"results": [{"id": 1,"title": "prueba c papu", "overview": "Esto es una prueba papu"},
#                     {"id": 2, "title": "prueba c papu2", "overview": "Esto es una prueba papu2"}]})["results"]
#         cards = []
#         for x in response:
#             # print(x['title'])
#             btn_id= f"btn_{str(x['id'])}"
#             cards.append(ui.div(
#                 ui.h3(x["title"], style="margin: 0;"),
#                 ui.div(
#                     ui.p(f"{str(x['overview'])}", style="margin-top: 5px;"), 
#                     ui.input_action_button(btn_id, "Ver info", style="width: 125px;"),
#                     style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;"
#                     ),
#                 style="padding: 10px; border: 1px solid #ddd; border-radius: 8px; margin-bottom: 10px;"
#                 ))

#         return cards

@render.text()
@reactive.event(input.buscar)
def buscar_pelicula():
    pelicula = input.peliculasInput()
    print(f"\nLa pelicula a buscar es: {pelicula}")


# @render.text()
# @reactive.event(input['btn_']) 
# def boton_pelicula():
#     print('clic')