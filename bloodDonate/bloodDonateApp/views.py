from django.shortcuts import render
from .models import *


import psycopg2
import boto3

from rest_framework.views import APIView
from rest_framework.response import Response



######################################################################
                                                                      
customhost = "databasebd.cmogv3rjeyml.eu-north-1.rds.amazonaws.com" #
customuser = "postgres"                                             #
custompass = "awscharan"                                            #
customdb = "bloodDonateApp_bloodDonateData"                         #
custombucket = "blooddonationbucket"                                #
customregion = "eu-north-1"                                         #
                                                                      
######################################################################


# psql --host=databasebd.cmogv3rjeyml.eu-north-1.rds.amazonaws.com --port=5432 --username=postgres -W

# Create your views here.
def index(request):
    return render(request, 'about.html')

def wbd(request):
    return render(request,'WBD.html')

def bad(request):
    return render(request,'BAD.html')

bucket = custombucket
region = customregion


engine = psycopg2.connect(
    database=customdb,
    user=customuser,
    password=custompass,
    host=customhost,
    port='5432'
)

def saveBAD(request):
    if request.method == "POST":
        fullName_Id = request.POST['fullNameId']
        mobileNumber_Id = request.POST['mobileNumberId']
        email_Id = request.POST['emailId']
        age_Id = request.POST['ageId']
        gender_Id = request.POST['genderId']
        bloodGroup_Id = request.POST['bloodGroupId']
        address_Id = request.POST['addressId']
        uploadCertificate_Id=request.POST['uploadCertificateId']
        # ob=bloodDonateData.objects.all()
        # certificate_file_name="bloodDonor_"+str(len(ob))
        # certificate_image_file = "https://awsmyfirstproject.s3.eu-north-1.amazonaws.com/{0}".format(certificate_file_name)
        # upload=bloodDonateData(full_name=fullName_Id,mobile_number=mobileNumber_Id,email_id=email_Id,age=age_Id,gender=gender_Id,blood_group=bloodGroup_Id,address=address_Id,upload_file=certificate_image_file)
        # upload.save()  
        
        if uploadCertificate_Id.filename == "":
            return "Please select a file"

        try:
            ob=bloodDonateData.objects.all()
            certificate_file_name="bloodDonor_"+str(len(ob))
            certificate_image_file = "https://awsmyfirstproject.s3.eu-north-1.amazonaws.com/{0}".format(certificate_file_name)
            upload=bloodDonateData(full_name=fullName_Id,mobile_number=mobileNumber_Id,email_id=email_Id,age=age_Id,gender=gender_Id,blood_group=bloodGroup_Id,address=address_Id,upload_file=certificate_image_file)
            s3 = boto3.resource('s3')

            try:
                print("Data inserted in MySQL RDS... uploading image to S3...")
                s3.Bucket(custombucket).put_object(Key=certificate_file_name, Body=uploadCertificate_Id)
                bucket_location = boto3.client('s3').get_bucket_location(Bucket=custombucket)
                s3_location = (bucket_location['LocationConstraint'])

                if s3_location is None:
                    s3_location = ''
                else:
                    s3_location = '-' + s3_location

                object_url = "https://s3{0}.amazonaws.com/{1}/{2}".format(
                    s3_location,
                    custombucket,
                    certificate_file_name)

            except Exception as e:
                return str(e)

        finally:
           upload.save()

        print("all modification done...")
        
    return render(request,'BAD.html')

def nb(request):
    return render(request,'NB.html')


class nbInfo(APIView):
    def get(self, request, format=None):
        nbObject = bloodDonateData.objects.values()
        nbResponse=[]
        for i in nbObject:
            nbResponse.append(i)
        return Response(nbResponse)

def cs(request):
    return render(request,'CS.html')