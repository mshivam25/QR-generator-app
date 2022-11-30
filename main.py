from kivymd.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
import qrcode
import plyer

from kivy.core.window import Window

Window.size = 360, 640


class Function(ScreenManager):
    def generate_qr_code(self, root):
        if self.ids.link_text.text != '' and self.ids.image_name.text != '':
            code = qrcode.QRCode(version=1.0, box_size=15, border=4)
            code.add_data(self.ids.link_text.text)
            code.make(fit=True)
            img = code.make_image(fill='Red', back_color='White')
            img.save(f'{self.ids.image_name.text}.jpg')
            plyer.notification.notify(
                title="QR code generator", message="QR code generated"
            )
        else:
            plyer.notification.notify(
                title='QR code generator', message='Qr code generated'
            )

    def view_image(self, root):
        self.ids.img_.source = f'{self.ids.image_name.text}.jpg'
        root.current = 'image'

    def make_another(self, root):
        self.ids.link_text.text = ''
        self.ids.image_name.text = ''
        root.current = 'first'


class Main(MDApp):
    Builder.load_file('layout.kv')

    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        return Function()


Main().run()
