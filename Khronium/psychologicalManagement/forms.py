from django import forms

class KEDSForm(forms.Form):
    abilityToConcentrate = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. I do not have any difficulty concentrating, and can read, watch TV and converse normally.'),
         ('1','1.'),
         ('2','2. I occasionally have difficulty keeping my thoughts together on things that would normally hold myattention.'),
         ('3','3.'),
         ('4','4. I have often difficulty concentrating.'),
         ('5','5.'),
         ('6','6. I cannot concentrate on anything at all.')
        ])
    memory = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. I remember names, dates, and what I am supposed to do.'),
         ('1','1.'),
         ('2','2. Sometimes I forget things that are not so important, but if I pull myself together I can usuallyremember. '),
         ('3','3.'),
         ('4','4. I often forget appointments or names of people whom I know very well.'),
         ('5','5.'),
         ('6','6. Every day, I forget important things or what I have promised to do.')
        ])
    physicalStamina = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. I feel the way I usually do and perform my daily physical activities or exercise as usual.'),
         ('1','1.'),
         ('2','2. I feel that physical effort is more exhausting than normal, but still move the way I usually do in this respect.'),
         ('3','3.'),
         ('4','4. I do not have the energy to exert myself physically. It is OK as long as I move at a normal phase, but I cannot increase my pace without becoming shaky and short of breath. '),
         ('5','5.'),
         ('6','6. I feel very weak and cannot even move short distances.')
        ])
    mentalStamina = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. I have just as much energy as usual. I do not have any particular difficult performing my daily activities.'),
         ('1','1.'),
         ('2','2. I can manage my everyday activities, but they take more energy and I am exhausted more quickly than usual. I need to take breaks more often than usual.'),
         ('3','3.'),
         ('4','4. I become inordinately tired when I attempt my daily activities and find social situations exhausting.'),
         ('5','5.'),
         ('6','6. I do not have the energy to do anything.')
        ])
    recovery = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. I do not have to rest during the day.'),
         ('1','1.'),
         ('2','2. I become tired during the day, but all I have to do is to take a little break in order to recover.'),
         ('3','3.'),
         ('4','4. I become tired during the day and need to take long breaks in order to feel fit.'),
         ('5','5.'),
         ('6','6. No matter how much I rest, it feels as if I am unable to recharge my batteries.')
        ])
    sleep = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. I sleep well and long enough. I usually feel thoroughly rested when I wake up after a night’s sleep.'),
         ('1','1.'),
         ('2','2. Sometimes, I sleep more restlessly than usual, or wake up during the night and have difficulty going back to sleep. Sometimes, I do not feel thoroughly rested when I wake up after a night’s sleep.'),
         ('3','3.'),
         ('4','4. I often sleep more restlessly than usual, or wake up during the night and have difficulty going back to sleep. I often have a feeling of not being thoroughly rested after a night’s sleep. '),
         ('5','5.'),
         ('6','6. I sleep superficially or restlessly every night. I never feel thoroughly rested after a night’s sleep.')
        ])
    hypersensitivityToSensoryImpressions = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. I do not think that my senses are more sensitive than usual.'),
         ('1','1.'),
         ('2','2. Sound or light or other sensory impressions are sometimes unpleasant.'),
         ('3','3.'),
         ('4','4. I often experience that sound, light or other sensory impressions are disturbing or unpleasant.'),
         ('5','5.'),
         ('6','6. Sound, light or other sensory impressions bother me so much that I withdraw in order to give my senses a chance to rest.')
        ])
    experienceOfDemands = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. I do what I am supposed to do or want to do without experiencing it as especially demanding or difficult.'),
         ('1','1.'),
         ('2','2. Sometimes I experience daily situations that I used to handle without any particular problem as demanding, leading to unease, or causing me to become more easily stressed.'),
         ('3','3.'),
         ('4','4. I often feel that situations that I previously handled without problem are now demanding and cause a strong feeling of uneasiness or stress.'),
         ('5','5.'),
         ('6','6. l experience nearly everything as demanding and cannot handle it at all.')
        ])
    irritationAndAnger = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. I do not feel that I am especially easily irritated.'),
         ('1','1.'),
         ('2','2. I am more impatient and easily irritated than usual, but the feeling quickly passes.'),
         ('3','3.'),
         ('4','4. I become more impatient and easily irritated than usual. Sometimes I lose control in a way that is unusual for me.'),
         ('5','5.'),
         ('6','6. I am often furious and have to make an enormous effort in order to restrain myself.')
        ])
    

class MADRSForm(forms.Form):
    apparentSadness = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. No sadness'),
         ('1','1.'),
         ('2','2. Looks dispirited but does brighten up without dificulty.'),
         ('3','3.'),
         ('4','4. Appears sad and unhappy most of the time.'),
         ('5','5.'),
         ('6','6. Looks miserable all the time. Extremely despondent.')
        ])
    reportedSadness = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. Occasional sadness in keeping with the circumstances.'),
         ('1','1.'),
         ('2','2. Sad or low but brightens up without dificulty.'),
         ('3','3.'),
         ('4','4. Pervasive feelings of sadness or gloominess. The mood is still influenced bu external circumstances.'),
         ('5','5.'),
         ('6','6. Continuous or unvarying sadness, misery or desponderncy.')
        ])
    innerTension = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. Placid. Only fleeting inner tension.'),
         ('1','1.'),
         ('2','2. Ocacasion feelings of edginess and ill-defined discomfort.'),
         ('3','3.'),
         ('4','4. Continuous feelings of inner tension or intermittent panic which the patient can only master with some difficulty.'),
         ('5','5.'),
         ('6','6. Unrelenting dred or anguish. Overwhelming panic.')
        ])
    reducedSleep = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. Sleeps as usual.'),
         ('1','1.'),
         ('2','2. Slight difficulty dropping off to sleep or slightly reduced, light or fitful sleep'),
         ('3','3.'),
         ('4','4. Sleep reduced or broken by at least two hours.'),
         ('5','5.'),
         ('6','6. Less than two or three hours sleep.')
        ])
    reducedAppetite = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. Normal or increased appetite.'),
         ('1','1.'),
         ('2','2. Slightly reduced appetite.'),
         ('3','3.'),
         ('4','4. No appetite. Food is tasteless.'),
         ('5','5.'),
         ('6','6. Needs persuassion to eat at all.')
        ])
    concentrationDifficulties = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. No difficulties in concentrating.'),
         ('1','1.'),
         ('2','2. Occasional difficulties in collecting one\'s thoughts.'),
         ('3','3.'),
         ('4','4. Difficulties in concentrating and sustaining thought which reduces ability to read or hold a conversasion.'),
         ('5','5.'),
         ('6','6. Unable to read or converse without great difficulty.')
        ])
    lassitude = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. Hardly any difficulty in getting started. No sluggishness.'),
         ('1','1.'),
         ('2','2. Difficulties in starting activities.'),
         ('3','3.'),
         ('4','4. Difficutlies in starting simple routine activities which are carried out with effort.'),
         ('5','5.'),
         ('6','6. Complete lassitude. Unable to do anything without help.')
        ])
    inabiityToFeel = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. Normal interesnt in the surroundings and in other people.'),
         ('1','1.'),
         ('2','2. Reduced ability to enjoy usual interests.'),
         ('3','3.'),
         ('4','4. Loss of interesnt in the surroundings. Loss of feelings for friends and acquaintances.'),
         ('5','5.'),
         ('6','6. The experience of being emotionally paralysed, inability to feel anger, grief or pleasure and a complete or even painful failure to feel for close relatives and friends.')
        ])
    passingThoughts = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. No pessimistic thoughts.'),
         ('1','1.'),
         ('2','2. Fluctuating ideas of failure, self-reproach or seld deprecation.'),
         ('3','3.'),
         ('4','4. Persistent self-accusation, or definite but stil rational ideas of guilt or sin. Increasingly pessimistic about the future.'),
         ('5','5.'),
         ('6','6. Delusions of ruin, remorse or unredeemable sin. Self-accusations which are absurd and unshakable.')
        ])
    suicidalThoughts = forms.ChoiceField(widget=forms.RadioSelect, choices=
        [('0','0. Enjoy life or takes it as it comes.'),
         ('1','1.'),
         ('2','2. Weary of life. Only fleeting suicidal thoughts.'),
         ('3','3.'),
         ('4','4. Probably better off dead. Suicidal thoughts are common, and suicide is considered as a possible solution, but without specific plans or intention.'),
         ('5','5.'),
         ('6','6. Explicit plans for suicide when there is an opportunity. Active preparations for suicide.')
        ])