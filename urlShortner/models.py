from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.
class Images(models.Model):
    qr_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=600)
    qr_codes = models.ImageField(upload_to="images", blank=True)

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB',(420,420),'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        filename = self.name
        filename = filename.split('/')
        print(filename)
        fname = f'qr_code-{filename}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_codes.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)    
