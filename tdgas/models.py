from django.db                  import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from .validators                import *


SHORT       = 50
BRIEF       = 100
MEDIUM      = 150
LONG_BRIEF  = 200
LONG        = 400
VERY_LONG   = 1000

DOG_TYPE = (
    ('0'    , 'Affenpinscher'),
    ('1'    , 'Afghan Hound'),
    ('2'    , 'Airedale Terrier'),
    ('3'    , 'Akita'),
    ('4'    , 'Alaskan Klee Kai'),
    ('5'    , 'Alaskan Malamute'),
    ('6'    , 'American Bulldog'),
    ('7'    , 'American English Coonhound'),
    ('8'    , 'American Eskimo Dog'),
    ('9'    , 'American Foxhound'),
    ('10'   , 'American Pit Bull Terrier'),
    ('11'   , 'American Staffordshire Terrier'),
    ('12'   , 'American Water Spaniel'),
    ('13'   , 'Anatolian Shepherd Dog'),
    ('14'   , 'Appenzeller Sennenhunde'),
    ('15'   , 'Australian Cattle Dog'),
    ('16'   , 'Australian Kelpie'),
    ('17'   , 'Australian Shepherd'),
    ('18'   , 'Australian Terrier'),
    ('19'   , 'Azawakh'),
    ('20'   , 'Barbet'),
    ('21'   , 'Basenji'),
    ('22'   , 'Basset Hound'),
    ('23'   , 'Beagle'),
    ('24'   , 'Bearded Collie'),
    ('25'   , 'Bedlington Terrier'),
    ('26'   , 'Belgian Malinois'),
    ('27'   , 'Belgian Sheepdog'),
    ('28'   , 'Belgian Tervuren'),
    ('29'   , 'Berger Picard'),
    ('30'   , 'Bernedoodle'),
    ('31'   , 'Bernese Mountain Dog'),
    ('32'   , 'Bichon Frise'),
    ('33'   , 'Black and Tan Coonhound'),
    ('34'   , 'Black Mouth Cur'),
    ('35'   , 'Black Russian Terrier'),
    ('36'   , 'Bloodhound'),
    ('37'   , 'Blue Lacy'),
    ('38'   , 'Bluetick Coonhound'),
    ('39'   , 'Boerboel'),
    ('40'   , 'Bolognese'),
    ('41'   , 'Border Collie'),
    ('42'   , 'Border Terrier'),
    ('43'   , 'Borzoi'),
    ('44'   , 'Boston Terrier'),
    ('45'   , 'Bouvier des Flandres'),
    ('46'   , 'Boxer'),
    ('47'   , 'Boykin Spaniel'),
    ('48'   , 'Bracco Italiano'),
    ('49'   , 'Briard'),
    ('50'   , 'Brittany'),
    ('51'   , 'Brussels Griffon'),
    ('52'   , 'Bull Terrier'),
    ('53'   , 'Bulldog'),
    ('54'   , 'Bullmastiff'),
    ('55'   , 'Cairn Terrier'),
    ('56'   , 'Canaan Dog'),
    ('57'   , 'Cane Corso'),
    ('58'   , 'Cardigan Welsh Corgi'),
    ('59'   , 'Catahoula Leopard Dog'),
    ('60'   , 'Caucasian Shepherd Dog'),
    ('61'   , 'Cavalier King Charles Spaniel'),
    ('62'   , 'Cesky Terrier'),
    ('63'   , 'Chesapeake Bay Retriever'),
    ('64'   , 'Chihuahua'),
    ('65'   , 'Chinese Crested'),
    ('66'   , 'Chinese Shar-Pei'),
    ('67'   , 'Chinook'),
    ('68'   , 'Chow Chow'),
    ('69'   , 'Clumber Spaniel'),
    ('70'   , 'Cockapoo'),
    ('71'   , 'Cocker Spaniel'),
    ('72'   , 'Collie'),
    ('73'   , 'Coton de Tulear'),
    ('74'   , 'Curly-Coated Retriever'),
    ('75'   , 'Dachshund'),
    ('76'   , 'Dalmatian'),
    ('77'   , 'Dandie Dinmont Terrier'),
    ('78'   , 'Doberman Pinscher'),
    ('79'   , 'Dogo Argentino'),
    ('80'   , 'Dogue de Bordeaux'),
    ('81'   , 'Dutch Shepherd'),
    ('82'   , 'English Cocker Spaniel'),
    ('83'   , 'English Foxhound'),
    ('84'   , 'English Setter'),
    ('85'   , 'English Springer Spaniel'),
    ('86'   , 'English Toy Spaniel'),
    ('87'   , 'Entlebucher Mountain Dog'),
    ('88'   , 'Field Spaniel'),
    ('89'   , 'Finnish Lapphund'),
    ('90'   , 'Finnish Spitz'),
    ('91'   , 'Flat-Coated Retriever'),
    ('92'   , 'Fox Terrier'),
    ('93'   , 'French Bulldog'),
    ('94'   , 'German Pinscher'),
    ('95'   , 'German Shepherd Dog'),
    ('96'   , 'German Shorthaired Pointer'),
    ('97'   , 'German Wirehaired Pointer'),
    ('98'   , 'Giant Schnauzer'),
    ('99'   , 'Glen of Imaal Terrier'),
    ('101'  , 'Goldador'),
    ('102'  , 'Golden Retriever'),
    ('103'  , 'Goldendoodle'),
    ('104'  , 'Gordon Setter'),
    ('105'  , 'Great Dane'),
    ('106'  , 'Great Pyrenees'),
    ('107'  , 'Greater Swiss Mountain Dog'),
    ('108'  , 'Greyhound'),
    ('109'  , 'Harrier'),
    ('110'  , 'Havanese'),
    ('111'  , 'Ibizan Hound'),
    ('112'  , 'Icelandic Sheepdog'),
    ('113'  , 'Irish Red and White Setter'),
    ('114'  , 'Irish Setter'),
    ('115'  , 'Irish Terrier'),
    ('116'  , 'Irish Water Spaniel'),
    ('117'  , 'Irish Wolfhound'),
    ('118'  , 'Italian Greyhound'),
    ('119'  , 'Jack Russell Terrier'),
    ('120'  , 'Japanese Chin'),
    ('121'  , 'Keeshond'),
    ('122'  , 'Kerry Blue Terrier'),
    ('123'  , 'Komondor'),
    ('124'  , 'Kooikerhondje'),
    ('125'  , 'Korean Jindo Dog'),
    ('126'  , 'Kuvasz'),
    ('127'  , 'Labradoodle'),
    ('128'  , 'Labrador Retriever'),
    ('129'  , 'Lakeland Terrier'),
    ('130'  , 'Lancashire Heeler'),
    ('131'  , 'Leonberger'),
    ('132'  , 'Lhasa Apso'),
    ('133'  , 'Lowchen'),
    ('134'  , 'Maltese'),
    ('135'  , 'Maltese Shih Tzu'),
    ('136'  , 'Maltipoo'),
    ('137'  , 'Manchester Terrier'),
    ('138'  , 'Mastiff'),
    ('139'  , 'Miniature Pinscher'),
    ('140'  , 'Miniature Schnauzer'),
    ('141'  , 'Mudi'),
    ('142'  , 'Mutt'),
    ('143'  , 'Neapolitan Mastiff'),
    ('144'  , 'Newfoundland'),
    ('145'  , 'Norfolk Terrier'),
    ('146'  , 'Norwegian Buhund'),
    ('147'  , 'Norwegian Elkhound'),
    ('148'  , 'Norwegian Lundehund'),
    ('149'  , 'Norwich Terrier'),
    ('150'  , 'Nova Scotia Duck Trolling Retriever'),
    ('151'  , 'Old English Sheepdog'),
    ('152'  , 'Otterhound'),
    ('153'  , 'Papillon'),
    ('154'  , 'Peekapoo'),
    ('155'  , 'Pekingese'),
    ('156'  , 'Pembroke Welsh Corgi'),
    ('157'  , 'Petit Basset Griffon Vendeen'),
    ('158'  , 'Pharaoh Hound'),
    ('159'  , 'Plott'),
    ('160'  , 'Pocket Beagle'),
    ('161'  , 'Pointer'),
    ('162'  , 'Polish Lowland Sheepdog'),
    ('163'  , 'Pomeranian'),
    ('164'  , 'Pomsky'),
    ('165'  , 'Poodle'),
    ('166'  , 'Portuguese Water Dog'),
    ('167'  , 'Pug'),
    ('168'  , 'Puggle'),
    ('169'  , 'Puli'),
    ('170'  , 'Pyrenean Shepherd'),
    ('171'  , 'Rat Terrier'),
    ('172'  , 'Redbone Coonhound'),
    ('173'  , 'Rhodesian Ridgeback'),
    ('174'  , 'Rottweiler'),
    ('175'  , 'Saint Bernard'),
    ('176'  , 'Saluki'),
    ('177'  , 'Samoyed'),
    ('178'  , 'Schipperke'),
    ('179'  , 'Schnoodle'),
    ('180'  , 'Scottish Deerhound'),
    ('181'  , 'Scottish Terrier'),
    ('182'  , 'Sealyham Terrier'),
    ('183'  , 'Shetland Sheepdog'),
    ('184'  , 'Shiba Inu'),
    ('185'  , 'Shih Tzu'),
    ('186'  , 'Siberian Husky'),
    ('187'  , 'Silky Terrier'),
    ('188'  , 'Skye Terrier'),
    ('189'  , 'Sloughi'),
    ('190'  , 'Small Munsterlander Pointer'),
    ('191'  , 'Soft Coated Wheaten Terrier'),
    ('192'  , 'Stabyhoun'),
    ('193'  , 'Staffordshire Bull Terrier'),
    ('194'  , 'Standard Schnauzer'),
    ('195'  , 'Sussex Spaniel'),
    ('196'  , 'Swedish Vallhund'),
    ('197'  , 'Tibetan Mastiff'),
    ('198'  , 'Tibetan Spaniel'),
    ('199'  , 'Tibetan Terrier'),
    ('200'  , 'Toy Fox Terrier'),
    ('201'  , 'Treeing Tennessee Brindle'),
    ('202'  , 'Treeing Walker Coonhound'),
    ('203'  , 'Vizsla'),
    ('204'  , 'Weimaraner'),
    ('205'  , 'Welsh Springer Spaniel'),
    ('206'  , 'Welsh Terrier'),
    ('207'  , 'West Highland White Terrier'),
    ('208'  , 'Whippet'),
    ('209'  , 'Wirehaired Pointing Griffon'),
    ('210'  , 'Xoloitzcuintli'),
    ('211'  , 'Yorkipoo'),
    ('212'  , 'Yorkshire Terrier'),
    ('213'  , 'Others')
)

class CustomUserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password = None, first_name = None, last_name = None):
        if not email:
            raise ValueError('Users must have a valid e-mail address.')
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        if not first_name:
            raise ValueError('Users must enter firstname.')
        user.first_name = first_name
        if not last_name:
            raise ValueError('Users must enter lastname.' )
        user.last_name  = last_name
        user.save(self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email       = email,
            password    = password,
        )
        user.is_superuser   = True
        user.is_admin       = True
        user.is_staff       = True
        user.save(using = self._db)
        return user


class User(AbstractUser):
    # Remove the default username field.
    username = None
    # Set the User to use email field for authentication.
    USERNAME_FIELD = 'email'
    # User fields.
    email             = models.EmailField   (max_length = SHORT, unique = True)
    first_name        = models.CharField    (max_length = SHORT, validators = [name_validator])
    last_name         = models.CharField    (max_length = SHORT, validators = [name_validator])
    address_street    = models.CharField    (max_length = BRIEF, null = True, blank = True)
    address_suburb    = models.CharField    (max_length = SHORT, null = True, blank = True)
    address_state     = models.CharField    (max_length = SHORT, null = True, blank = True)
    address_postcode  = models.CharField    (max_length = SHORT, null = True, blank = True)
    address_country   = models.CharField    (max_length = SHORT, null = True, blank = True)

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

class Contact(models.Model):
    CONTACT_TYPE = (
        ('mobile', 'Mobile'),
        ('home'  , 'Home'  ),
        ('work'  , 'Work'  )
    )
    user            = models.ForeignKey     (User, on_delete = models.CASCADE)
    contact_type    = models.CharField      (max_length = SHORT, choices = CONTACT_TYPE)
    phone_number    = models.CharField      (max_length = SHORT, null = True, blank = True)

    def __str__(self):
        return self.user.email + ' - ' + self.contact_type

class Dog(models.Model):
    owner           = models.ForeignKey     (User, on_delete = models.CASCADE)
    dog_name        = models.CharField      (max_length = SHORT)
    breed           = models.CharField      (max_length = SHORT, choices = DOG_TYPE)
    date_of_birth   = models.DateField      ()

class Appointment(models.Model):
    GROOM_TYPE = (
        ('1', 'Wash only'),
        ('2', 'Wash and nail clipping'),
        ('3', 'Deluxe grooming')
    )

    PAY_STATUS = (
        ('1', 'Paid'),
        ('2', 'To be paid')
    )

    subscriber              = models.ForeignKey     (User, on_delete = models.CASCADE)
    groom_dog               = models.ForeignKey     (Dog , on_delete = models.CASCADE)
    groom_type              = models.CharField      (max_length = SHORT, choices = GROOM_TYPE)
    order_price             = models.DecimalField   (max_digits = 5    , decimal_places = 2)
    payment_status          = models.CharField      (max_length = SHORT, choices = PAY_STATUS)
    comment                 = models.CharField      (max_length = LONG , null = True, blank = True)
    appointment_datetime    = models.DateTimeField  ()
    create_datetime         = models.DateTimeField  (auto_now_add = True)
