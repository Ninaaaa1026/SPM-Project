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
    ('Affenpinscher'                       , 'Affenpinscher'                       ),
    ('Afghan Hound'                        , 'Afghan Hound'                        ),
    ('Airedale Terrier'                    , 'Airedale Terrier'                    ),
    ('Akita'                               , 'Akita'                               ),
    ('Alaskan Klee Kai'                    , 'Alaskan Klee Kai'                    ),
    ('Alaskan Malamute'                    , 'Alaskan Malamute'                    ),
    ('American Bulldog'                    , 'American Bulldog'                    ),
    ('American English Coonhound'          , 'American English Coonhound'          ),
    ('American Eskimo Dog'                 , 'American Eskimo Dog'                 ),
    ('American Foxhound'                   , 'American Foxhound'                   ),
    ('American Pit Bull Terrier'           , 'American Pit Bull Terrier'           ),
    ('American Staffordshire Terrier'      , 'American Staffordshire Terrier'      ),
    ('American Water Spaniel'              , 'American Water Spaniel'              ),
    ('Anatolian Shepherd Dog'              , 'Anatolian Shepherd Dog'              ),
    ('Appenzeller Sennenhunde'             , 'Appenzeller Sennenhunde'             ),
    ('Australian Cattle Dog'               , 'Australian Cattle Dog'               ),
    ('Australian Kelpie'                   , 'Australian Kelpie'                   ),
    ('Australian Shepherd'                 , 'Australian Shepherd'                 ),
    ('Australian Terrier'                  , 'Australian Terrier'                  ),
    ('Azawakh'                             , 'Azawakh'                             ),
    ('Barbet'                              , 'Barbet'                              ),
    ('Basenji'                             , 'Basenji'                             ),
    ('Basset Hound'                        , 'Basset Hound'                        ),
    ('Beagle'                              , 'Beagle'                              ),
    ('Bearded Collie'                      , 'Bearded Collie'                      ),
    ('Bedlington Terrier'                  , 'Bedlington Terrier'                  ),
    ('Belgian Malinois'                    , 'Belgian Malinois'                    ),
    ('Belgian Sheepdog'                    , 'Belgian Sheepdog'                    ),
    ('Belgian Tervuren'                    , 'Belgian Tervuren'                    ),
    ('Berger Picard'                       , 'Berger Picard'                       ),
    ('Bernedoodle'                         , 'Bernedoodle'                         ),
    ('Bernese Mountain Dog'                , 'Bernese Mountain Dog'                ),
    ('Bichon Frise'                        , 'Bichon Frise'                        ),
    ('Black and Tan Coonhound'             , 'Black and Tan Coonhound'             ),
    ('Black Mouth Cur'                     , 'Black Mouth Cur'                     ),
    ('Black Russian Terrier'               , 'Black Russian Terrier'               ),
    ('Bloodhound'                          , 'Bloodhound'                          ),
    ('Blue Lacy'                           , 'Blue Lacy'                           ),
    ('Bluetick Coonhound'                  , 'Bluetick Coonhound'                  ),
    ('Boerboel'                            , 'Boerboel'                            ),
    ('Bolognese'                           , 'Bolognese'                           ),
    ('Border Collie'                       , 'Border Collie'                       ),
    ('Border Terrier'                      , 'Border Terrier'                      ),
    ('Borzoi'                              , 'Borzoi'                              ),
    ('Boston Terrier'                      , 'Boston Terrier'                      ),
    ('Bouvier des Flandres'                , 'Bouvier des Flandres'                ),
    ('Boxer'                               , 'Boxer'                               ),
    ('Boykin Spaniel'                      , 'Boykin Spaniel'                      ),
    ('Bracco Italiano'                     , 'Bracco Italiano'                     ),
    ('Briard'                              , 'Briard'                              ),
    ('Brittany'                            , 'Brittany'                            ),
    ('Brussels Griffon'                    , 'Brussels Griffon'                    ),
    ('Bull Terrier'                        , 'Bull Terrier'                        ),
    ('Bulldog'                             , 'Bulldog'                             ),
    ('Bullmastiff'                         , 'Bullmastiff'                         ),
    ('Cairn Terrier'                       , 'Cairn Terrier'                       ),
    ('Canaan Dog'                          , 'Canaan Dog'                          ),
    ('Cane Corso'                          , 'Cane Corso'                          ),
    ('Cardigan Welsh Corgi'                , 'Cardigan Welsh Corgi'                ),
    ('Catahoula Leopard Dog'               , 'Catahoula Leopard Dog'               ),
    ('Caucasian Shepherd Dog'              , 'Caucasian Shepherd Dog'              ),
    ('Cavalier King Charles Spaniel'       , 'Cavalier King Charles Spaniel'       ),
    ('Cesky Terrier'                       , 'Cesky Terrier'                       ),
    ('Chesapeake Bay Retriever'            , 'Chesapeake Bay Retriever'            ),
    ('Chihuahua'                           , 'Chihuahua'                           ),
    ('Chinese Crested'                     , 'Chinese Crested'                     ),
    ('Chinese Shar-Pei'                    , 'Chinese Shar-Pei'                    ),
    ('Chinook'                             , 'Chinook'                             ),
    ('Chow Chow'                           , 'Chow Chow'                           ),
    ('Clumber Spaniel'                     , 'Clumber Spaniel'                     ),
    ('Cockapoo'                            , 'Cockapoo'                            ),
    ('Cocker Spaniel'                      , 'Cocker Spaniel'                      ),
    ('Collie'                              , 'Collie'                              ),
    ('Coton de Tulear'                     , 'Coton de Tulear'                     ),
    ('Curly-Coated Retriever'              , 'Curly-Coated Retriever'              ),
    ('Dachshund'                           , 'Dachshund'                           ),
    ('Dalmatian'                           , 'Dalmatian'                           ),
    ('Dandie Dinmont Terrier'              , 'Dandie Dinmont Terrier'              ),
    ('Doberman Pinscher'                   , 'Doberman Pinscher'                   ),
    ('Dogo Argentino'                      , 'Dogo Argentino'                      ),
    ('Dogue de Bordeaux'                   , 'Dogue de Bordeaux'                   ),
    ('Dutch Shepherd'                      , 'Dutch Shepherd'                      ),
    ('English Cocker Spaniel'              , 'English Cocker Spaniel'              ),
    ('English Foxhound'                    , 'English Foxhound'                    ),
    ('English Setter'                      , 'English Setter'                      ),
    ('English Springer Spaniel'            , 'English Springer Spaniel'            ),
    ('English Toy Spaniel'                 , 'English Toy Spaniel'                 ),
    ('Entlebucher Mountain Dog'            , 'Entlebucher Mountain Dog'            ),
    ('Field Spaniel'                       , 'Field Spaniel'                       ),
    ('Finnish Lapphund'                    , 'Finnish Lapphund'                    ),
    ('Finnish Spitz'                       , 'Finnish Spitz'                       ),
    ('Flat-Coated Retriever'               , 'Flat-Coated Retriever'               ),
    ('Fox Terrier'                         , 'Fox Terrier'                         ),
    ('French Bulldog'                      , 'French Bulldog'                      ),
    ('German Pinscher'                     , 'German Pinscher'                     ),
    ('German Shepherd Dog'                 , 'German Shepherd Dog'                 ),
    ('German Shorthaired Pointer'          , 'German Shorthaired Pointer'          ),
    ('German Wirehaired Pointer'           , 'German Wirehaired Pointer'           ),
    ('Giant Schnauzer'                     , 'Giant Schnauzer'                     ),
    ('Glen of Imaal Terrier'               , 'Glen of Imaal Terrier'               ),
    ('Goldador'                            , 'Goldador'                            ),
    ('Golden Retriever'                    , 'Golden Retriever'                    ),
    ('Goldendoodle'                        , 'Goldendoodle'                        ),
    ('Gordon Setter'                       , 'Gordon Setter'                       ),
    ('Great Dane'                          , 'Great Dane'                          ),
    ('Great Pyrenees'                      , 'Great Pyrenees'                      ),
    ('Greater Swiss Mountain Dog'          , 'Greater Swiss Mountain Dog'          ),
    ('Greyhound'                           , 'Greyhound'                           ),
    ('Harrier'                             , 'Harrier'                             ),
    ('Havanese'                            , 'Havanese'                            ),
    ('Ibizan Hound'                        , 'Ibizan Hound'                        ),
    ('Icelandic Sheepdog'                  , 'Icelandic Sheepdog'                  ),
    ('Irish Red and White Setter'          , 'Irish Red and White Setter'          ),
    ('Irish Setter'                        , 'Irish Setter'                        ),
    ('Irish Terrier'                       , 'Irish Terrier'                       ),
    ('Irish Water Spaniel'                 , 'Irish Water Spaniel'                 ),
    ('Irish Wolfhound'                     , 'Irish Wolfhound'                     ),
    ('Italian Greyhound'                   , 'Italian Greyhound'                   ),
    ('Jack Russell Terrier'                , 'Jack Russell Terrier'                ),
    ('Japanese Chin'                       , 'Japanese Chin'                       ),
    ('Keeshond'                            , 'Keeshond'                            ),
    ('Kerry Blue Terrier'                  , 'Kerry Blue Terrier'                  ),
    ('Komondor'                            , 'Komondor'                            ),
    ('Kooikerhondje'                       , 'Kooikerhondje'                       ),
    ('Korean Jindo Dog'                    , 'Korean Jindo Dog'                    ),
    ('Kuvasz'                              , 'Kuvasz'                              ),
    ('Labradoodle'                         , 'Labradoodle'                         ),
    ('Labrador Retriever'                  , 'Labrador Retriever'                  ),
    ('Lakeland Terrier'                    , 'Lakeland Terrier'                    ),
    ('Lancashire Heeler'                   , 'Lancashire Heeler'                   ),
    ('Leonberger'                          , 'Leonberger'                          ),
    ('Lhasa Apso'                          , 'Lhasa Apso'                          ),
    ('Lowchen'                             , 'Lowchen'                             ),
    ('Maltese'                             , 'Maltese'                             ),
    ('Maltese Shih Tzu'                    , 'Maltese Shih Tzu'                    ),
    ('Maltipoo'                            , 'Maltipoo'                            ),
    ('Manchester Terrier'                  , 'Manchester Terrier'                  ),
    ('Mastiff'                             , 'Mastiff'                             ),
    ('Miniature Pinscher'                  , 'Miniature Pinscher'                  ),
    ('Miniature Schnauzer'                 , 'Miniature Schnauzer'                 ),
    ('Mudi'                                , 'Mudi'                                ),
    ('Mutt'                                , 'Mutt'                                ),
    ('Neapolitan Mastiff'                  , 'Neapolitan Mastiff'                  ),
    ('Newfoundland'                        , 'Newfoundland'                        ),
    ('Norfolk Terrier'                     , 'Norfolk Terrier'                     ),
    ('Norwegian Buhund'                    , 'Norwegian Buhund'                    ),
    ('Norwegian Elkhound'                  , 'Norwegian Elkhound'                  ),
    ('Norwegian Lundehund'                 , 'Norwegian Lundehund'                 ),
    ('Norwich Terrier'                     , 'Norwich Terrier'                     ),
    ('Nova Scotia Duck Trolling Retriever' , 'Nova Scotia Duck Trolling Retriever' ),
    ('Old English Sheepdog'                , 'Old English Sheepdog'                ),
    ('Otterhound'                          , 'Otterhound'                          ),
    ('Papillon'                            , 'Papillon'                            ),
    ('Peekapoo'                            , 'Peekapoo'                            ),
    ('Pekingese'                           , 'Pekingese'                           ),
    ('Pembroke Welsh Corgi'                , 'Pembroke Welsh Corgi'                ),
    ('Petit Basset Griffon Vendeen'        , 'Petit Basset Griffon Vendeen'        ),
    ('Pharaoh Hound'                       , 'Pharaoh Hound'                       ),
    ('Plott'                               , 'Plott'                               ),
    ('Pocket Beagle'                       , 'Pocket Beagle'                       ),
    ('Pointer'                             , 'Pointer'                             ),
    ('Polish Lowland Sheepdog'             , 'Polish Lowland Sheepdog'             ),
    ('Pomeranian'                          , 'Pomeranian'                          ),
    ('Pomsky'                              , 'Pomsky'                              ),
    ('Poodle'                              , 'Poodle'                              ),
    ('Portuguese Water Dog'                , 'Portuguese Water Dog'                ),
    ('Pug'                                 , 'Pug'                                 ),
    ('Puggle'                              , 'Puggle'                              ),
    ('Puli'                                , 'Puli'                                ),
    ('Pyrenean Shepherd'                   , 'Pyrenean Shepherd'                   ),
    ('Rat Terrier'                         , 'Rat Terrier'                         ),
    ('Redbone Coonhound'                   , 'Redbone Coonhound'                   ),
    ('Rhodesian Ridgeback'                 , 'Rhodesian Ridgeback'                 ),
    ('Rottweiler'                          , 'Rottweiler'                          ),
    ('Saint Bernard'                       , 'Saint Bernard'                       ),
    ('Saluki'                              , 'Saluki'                              ),
    ('Samoyed'                             , 'Samoyed'                             ),
    ('Schipperke'                          , 'Schipperke'                          ),
    ('Schnoodle'                           , 'Schnoodle'                           ),
    ('Scottish Deerhound'                  , 'Scottish Deerhound'                  ),
    ('Scottish Terrier'                    , 'Scottish Terrier'                    ),
    ('Sealyham Terrier'                    , 'Sealyham Terrier'                    ),
    ('Shetland Sheepdog'                   , 'Shetland Sheepdog'                   ),
    ('Shiba Inu'                           , 'Shiba Inu'                           ),
    ('Shih Tzu'                            , 'Shih Tzu'                            ),
    ('Siberian Husky'                      , 'Siberian Husky'                      ),
    ('Silky Terrier'                       , 'Silky Terrier'                       ),
    ('Skye Terrier'                        , 'Skye Terrier'                        ),
    ('Sloughi'                             , 'Sloughi'                             ),
    ('Small Munsterlander Pointer'         , 'Small Munsterlander Pointer'         ),
    ('Soft Coated Wheaten Terrier'         , 'Soft Coated Wheaten Terrier'         ),
    ('Stabyhoun'                           , 'Stabyhoun'                           ),
    ('Staffordshire Bull Terrier'          , 'Staffordshire Bull Terrier'          ),
    ('Standard Schnauzer'                  , 'Standard Schnauzer'                  ),
    ('Sussex Spaniel'                      , 'Sussex Spaniel'                      ),
    ('Swedish Vallhund'                    , 'Swedish Vallhund'                    ),
    ('Tibetan Mastiff'                     , 'Tibetan Mastiff'                     ),
    ('Tibetan Spaniel'                     , 'Tibetan Spaniel'                     ),
    ('Tibetan Terrier'                     , 'Tibetan Terrier'                     ),
    ('Toy Fox Terrier'                     , 'Toy Fox Terrier'                     ),
    ('Treeing Tennessee Brindle'           , 'Treeing Tennessee Brindle'           ),
    ('Treeing Walker Coonhound'            , 'Treeing Walker Coonhound'            ),
    ('Vizsla'                              , 'Vizsla'                              ),
    ('Weimaraner'                          , 'Weimaraner'                          ),
    ('Welsh Springer Spaniel'              , 'Welsh Springer Spaniel'              ),
    ('Welsh Terrier'                       , 'Welsh Terrier'                       ),
    ('West Highland White Terrier'         , 'West Highland White Terrier'         ),
    ('Whippet'                             , 'Whippet'                             ),
    ('Wirehaired Pointing Griffon'         , 'Wirehaired Pointing Griffon'         ),
    ('Xoloitzcuintli'                      , 'Xoloitzcuintli'                      ),
    ('Yorkipoo'                            , 'Yorkipoo'                            ),
    ('Yorkshire Terrier'                   , 'Yorkshire Terrier'                   ),
    ('Others'                              , 'Others'                              )
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

    def __str__(self):
        return self.owner.first_name + ' - ' + self.dog_name

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
