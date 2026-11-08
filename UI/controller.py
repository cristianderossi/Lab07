import flet as ft
from UI.view import View
from model.model import Model


'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO

    def popola_dropdown(self):

        self._view.tendina_libri.options.append(ft.dropdown.Option(key="none",text="nessun filtro"))
        libri=self._model.get_generi()
        for libro in libri:
            self._view.tendina_libri.options.append(ft.dropdown.Option(key=libro,text=libro))


        self._view.tendina_biblioteca.options.append(ft.dropdown.Option(key="none",text="nessun filtro"))
        biblioteca=self._model.get_biblioteche()
        for b in biblioteca:
            self._view.tendina_biblioteca.options.append(ft.dropdown.Option(key=str(b.id),text=b.nome))

    # CALLBACKS DROPDOWN
    # TODO

    def on_genere_select(self,e):
        v=e.control.value
        if v is None or v=="none":
            self.genere_selezionato=None
        else:
            self.genere_selezionato=v

    def on_biblioteca_select(self,e):
        v=e.control.value
        if v is None or v=="none":
            self.biblioteca_selezionata=None
        else:
            self.biblioteca_selezionata=int(v)




    # AZIONE: MOSTRA LIBRI
    # TODO








