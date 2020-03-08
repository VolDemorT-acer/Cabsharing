import pyrebase  


firebaseConfig = {
  "apiKey": "AIzaSyAIgNPNt_MdPZUKcfcp23CPQ_Dss1v7whw",
  "authDomain": "cab-sharing-270218.firebaseapp.com",
  "databaseURL": "https://cab-sharing-270218.firebaseio.com",
  "projectId": "cab-sharing-270218",
  "storageBucket": "cab-sharing-270218.appspot.com",
  "messagingSenderId": "252174418134",
  "appId": "1:252174418134:web:adbbbe331bae402609c977",
  "measurementId": "G-MC2VLLWWKR"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth1=firebase.auth()
#user=auth1.sign_in_with_email_and_password("email@usedforautheticatoon.com","FstrongPasswordHere")

db=firebase.database() 