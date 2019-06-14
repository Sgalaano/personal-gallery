from django.test import TestCase
from .models import Uploader,Photos,tags
import datetime as dt

# Create your tests here.
class UploaderTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.galaano= Uploader(first_name = 'Galaano', last_name ='Suleiman', email ='sgalaano@gmail.com')
     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.galaano,Uploader))
     # Testing Save Method
    def test_save_method(self):
        self.galaano.save_uploader()
        uploader = Uploader.objects.all()
        self.assertTrue(len(uploader) > 0)

class PhotosTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.galaano= Uploader(first_name = 'Galaano', last_name ='Suleiman', email ='sgalaano@gmail.com')
        self.galaano.save_uploader()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_photos= Photos(title = 'Test Photos',post = 'This is a random test Post',editor = self.galaano)
        self.new_photos.save()

        self.new_photos.tags.add(self.new_tag)

    def tearDown(self):
        Uploader.objects.all().delete()
        tags.objects.all().delete()
        Photos.objects.all().delete()

    def test_get_pictures_today(self):
        today_pictures = Photos.todays_pictures()
        self.assertTrue(len(today_pictures)>0)
    
    def test_get_pictures_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        pictures_by_date = Photos.days_pictures(date)
        self.assertTrue(len(pictures_by_date) == 0)