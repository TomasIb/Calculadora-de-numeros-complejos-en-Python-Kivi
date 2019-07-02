from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty
from kivymd.theming import ThemeManager
from kivymd.button import MDIconButton
from kivymd.theming import ThemeManager
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivy.config import Config
from complex_calculator import ComplexCalculator

content = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import SingleLineTextField kivymd.textfields.SingleLineTextField
#:import MDRaisedButton  kivymd.button.MDRaisedButton


BoxLayout:
    orientation: 'vertical'
    Toolbar:
        id: toolbar
        title: 'Calculadora de Números Complejos'
        background_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        

    ScrollView:
        do_scroll_x: False
        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: dp(250)
            halign: 'center'
           
        
            MDLabel:
                font_style: 'Body2'
                theme_text_color: 'Primary'
                text: " Ingrese la expresión:"
                halign: 'center'
                size_hint_y: None

            SingleLineTextField:
                id: expression
                hint_text: "Ejemplo: 2,2+3,7*[3,3/2,9+4,7.8]"
                size_hint_x: 0.7
                pos_hint: {'center_x': 0.5, 'center_y': 0.7}
     
            
            MDRaisedButton:
                id: button
                size_hint: None, None
                size: 3 * dp(48), dp(48)
                pos_hint: {'center_x': 0.5, 'center_y': 0.7}
                text: " ¡Calcular!"   
                on_press: app.get_value(expression.text)  
            
'''

class Content(GridLayout):
    def __init__(self,**kwargs):
        super(Content,self).__init__(**kwargs)
        self.cols = 2
        contentWidget = Builder.load_string(content)
        self.add_widget(contentWidget)
    
class CalculatorApp(App):
    theme_cls = ThemeManager()
    theme_cls.theme_style = 'Dark'
    nav_drawer = ObjectProperty()
    
           
    def build(self):
        self.content_widgets = Content()
        return self.content_widgets

    def get_value(self, text):
        self.value = text
        calculator = ComplexCalculator()
       
        result,initial_expression = calculator.calculate(text)
        
        if(result == False):
           self.error_dialog()
        else:
            expression_show = ' '.join([str(elem) for elem in initial_expression ])   
            self.success_dialog(result,expression_show)
    

    def success_dialog(self,result,expression_show):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Expresion ingresada:  "+str(expression_show),
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Resultado:  "+str(result),
                               content=content,
                               size_hint=(.8, None),
                               height=100,
                               auto_dismiss=False)

        self.dialog.add_action_button("Cerrar",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()
        
    def error_dialog(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="Error al ingresar la expresión",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Error",
                               content=content,
                               size_hint=(.8, None),
                               height=100,
                               auto_dismiss=False)

        self.dialog.add_action_button("Cerrar",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()
       

if __name__ == "__main__":
    CalculatorApp().run()
