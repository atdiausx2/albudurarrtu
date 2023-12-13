from flask import Blueprint, request, abort, jsonify
from .models import PipedriveLog, PipedriveDeal, PipedrivePerson, PipedriveNote, PipedriveActivity, ClientsOtoLog, PipedriveUsers
from . import db   ##means from __init__.py import db
import datetime
import requests
from collections import defaultdict
api = Blueprint('api', __name__)
import pandas as pd

API_KEY = '0b1fbae4-c824-4e1f-a96e-a086c132fff2'
API_KEY_ADMIN_UPDATE_GENERATED_ENERGY_VOLUME = '212f2a7610fbec74f9e4a9c85ef07c792f46a594'

# @api.route('/pipedrive-webhook-person-changed', methods=['POST'])
# ##@login_required
# def get_webhook_about_person_changed():

#     if request.method == 'POST':
#         provided_api_key = request.headers.get('api-token')

#         if not provided_api_key or provided_api_key != API_KEY:
#             abort(401, description='Unauthorized: Invalid API Key')

#         oto_crm_data = str(request.json)

#         utc_now = datetime.datetime.utcnow()
#         utc_now_lv = utc_now + datetime.timedelta(hours=2)

#         new_oto_crm_log = ClientsOtoLog(
#         ClientsOtoJson = oto_crm_data
#         ,CreatedDateTime = utc_now_lv
#         )
#         db.session.add(new_oto_crm_log)

#         response = {'message': 'Data received successfully'}

#     db.session.commit()

#     return jsonify(response), 200



@api.route('/api-jb-crm', methods=['POST'])
##@login_required
def api_jb_crm():

    if request.method == 'POST':
        provided_api_key = request.headers.get('api-token')

        if not provided_api_key or provided_api_key != API_KEY:
            abort(401, description='Unauthorized: Invalid API Key')

        oto_crm_data = str(request.json)

        utc_now = datetime.datetime.utcnow()
        utc_now_lv = utc_now + datetime.timedelta(hours=2)

        new_oto_crm_log = ClientsOtoLog(
        ClientsOtoJson = oto_crm_data
        ,CreatedDateTime = utc_now_lv
        )
        db.session.add(new_oto_crm_log)

        response = {'message': 'Data received successfully'}

    db.session.commit()

    return jsonify(response), 200


@api.route('/pipedrive-webhook', methods=['POST'])
##@login_required
def get_pipedrive_webhook():

    if request.method == 'POST':

        pipedrive_webhook_request = request.json

        pipedrive_webhook_json_meta = pipedrive_webhook_request['meta']
        pipedrive_webhook_json_data = pipedrive_webhook_request['data']
        pipedrive_webhook_json_previous = pipedrive_webhook_request['previous']

        pipedrive_webhook_json_meta_id = pipedrive_webhook_json_meta['id']
        pipedrive_webhook_json_meta_entity = pipedrive_webhook_json_meta['entity']
        pipedrive_webhook_json_meta_entity_id = pipedrive_webhook_json_meta['entity_id']
        pipedrive_webhook_json_meta_action = pipedrive_webhook_json_meta['action']
        pipedrive_webhook_json_meta_user_id = pipedrive_webhook_json_meta['user_id']
        pipedrive_webhook_json_meta_timestamp = pipedrive_webhook_json_meta['timestamp']


        new_pipedrive_log = PipedriveLog(
            MetaID = pipedrive_webhook_json_meta_id
            ,PipedriveWebhookJson = str(pipedrive_webhook_request)
            )
        db.session.add(new_pipedrive_log)


        if pipedrive_webhook_json_meta_entity == 'user':
          if pipedrive_webhook_json_meta_action == 'create':
        # there is not such actions as to delete the user in pipedrive
            pipedrive_webhook_json_data_add_time = pipedrive_webhook_json_previous['add_time']
            pipedrive_webhook_json_data_creator_user_id = pipedrive_webhook_json_previous['creator_user_id']
            # "active_flag": true,
            # pipedrive_webhook_json_data_is_active = pipedrive_webhook_json_previous['active_flag']
            pipedrive_webhook_json_data_email = pipedrive_webhook_json_previous['email']
            # "email": "sample@mailforspam.com",
            pipedrive_webhook_json_data_update_time = pipedrive_webhook_json_previous['modified']
            pipedrive_webhook_json_data_user_name = pipedrive_webhook_json_previous['name']
            pipedrive_webhook_json_data_user_id = pipedrive_webhook_json_previous['id']

            new_PipedriveUser = PipedriveUsers(
    PipedriveUsersPK = pipedrive_webhook_json_data_user_id,
    PipedriveUserName = pipedrive_webhook_json_data_user_name,
    PipedriveUserEmail =pipedrive_webhook_json_data_email,
    # by default not assign
    AssignClients = 0,
    # by default as sales person
    SalesPerson = 1,
    # by default to 2. department
    PipedriveTeamPK = 2,
    PipedriveSalaryPK = 0,
    CreatedDateTime = pipedrive_webhook_json_data_add_time,
    UpdatedDateTime = pipedrive_webhook_json_data_update_time
            )
            db.session.add(new_PipedriveUser)

        if pipedrive_webhook_json_meta_entity == 'deal':
            if pipedrive_webhook_json_meta_action == 'delete':
                pipedrive_webhook_json_data_add_time = pipedrive_webhook_json_previous['add_time']
                pipedrive_webhook_json_data_creator_user_id = pipedrive_webhook_json_previous['creator_user_id']
                try:
                    pipedrive_webhook_json_data_lost_reason = pipedrive_webhook_json_previous['lost_reason']
                except:
                    pipedrive_webhook_json_data_lost_reason = ''
                pipedrive_webhook_json_data_owner_id = pipedrive_webhook_json_previous['owner_id']
                pipedrive_webhook_json_data_person_id = pipedrive_webhook_json_previous['person_id']
                pipedrive_webhook_json_data_pipeline_id = pipedrive_webhook_json_previous['pipeline_id']
                pipedrive_webhook_json_data_stage_id = pipedrive_webhook_json_previous['stage_id']
                pipedrive_webhook_json_data_status = pipedrive_webhook_json_previous['status']
                pipedrive_webhook_json_data_value = pipedrive_webhook_json_previous['value']

            else:
                pipedrive_webhook_json_data_add_time = pipedrive_webhook_json_data['add_time']
                pipedrive_webhook_json_data_creator_user_id = pipedrive_webhook_json_data['creator_user_id']
                try:
                    pipedrive_webhook_json_data_lost_reason = pipedrive_webhook_json_data['lost_reason']
                except:
                    pipedrive_webhook_json_data_lost_reason = ''
                pipedrive_webhook_json_data_owner_id = pipedrive_webhook_json_data['owner_id']
                pipedrive_webhook_json_data_person_id = pipedrive_webhook_json_data['person_id']
                pipedrive_webhook_json_data_pipeline_id = pipedrive_webhook_json_data['pipeline_id']
                pipedrive_webhook_json_data_stage_id = pipedrive_webhook_json_data['stage_id']
                pipedrive_webhook_json_data_status = pipedrive_webhook_json_data['status']
                pipedrive_webhook_json_data_value = pipedrive_webhook_json_data['value']

            new_PipedriveDeal = PipedriveDeal(
                MetaID = pipedrive_webhook_json_meta_id
                ,MetaEntity = pipedrive_webhook_json_meta_entity
                ,MetaEntityID = pipedrive_webhook_json_meta_entity_id
                ,MetaAction = pipedrive_webhook_json_meta_action
                ,MetaUserID = pipedrive_webhook_json_meta_user_id
                ,MetaCreatedDateTime = pipedrive_webhook_json_meta_timestamp
                ,CreatorUserID = pipedrive_webhook_json_data_creator_user_id
                ,OwnerID = pipedrive_webhook_json_data_owner_id
                ,PersonID = pipedrive_webhook_json_data_person_id
                ,PipelineID = pipedrive_webhook_json_data_pipeline_id
                ,StageID = pipedrive_webhook_json_data_stage_id
                ,DealAddedTime = pipedrive_webhook_json_data_add_time
                ,DealLostReason = pipedrive_webhook_json_data_lost_reason
                ,DealStatus = pipedrive_webhook_json_data_status
                ,DealProductValue = pipedrive_webhook_json_data_value
            )
            db.session.add(new_PipedriveDeal)

        if pipedrive_webhook_json_meta_entity == 'person':
            if pipedrive_webhook_json_meta_action == 'delete':
                pipedrive_webhook_json_data_label = pipedrive_webhook_json_previous['label']
                pipedrive_webhook_json_data_owner_id = pipedrive_webhook_json_previous['owner_id']
                pipedrive_webhook_json_data_first_name = pipedrive_webhook_json_previous['first_name']
                try:
                    pipedrive_webhook_json_data_phone = pipedrive_webhook_json_previous['phones'][0]['value']
                except:
                    pipedrive_webhook_json_data_phone = ''
                try:
                    pipedrive_webhook_json_data_email = pipedrive_webhook_json_previous['emails'][0]['value']
                except:
                    pipedrive_webhook_json_data_email = ''

            else:
                pipedrive_webhook_json_data_label = pipedrive_webhook_json_data['label']
                pipedrive_webhook_json_data_owner_id = pipedrive_webhook_json_data['owner_id']
                pipedrive_webhook_json_data_first_name = pipedrive_webhook_json_data['first_name']
                try:
                    pipedrive_webhook_json_data_phone = pipedrive_webhook_json_data['phones'][0]['value']
                except:
                    pipedrive_webhook_json_data_phone = ''
                try:
                    pipedrive_webhook_json_data_email = pipedrive_webhook_json_data['emails'][0]['value']
                except:
                    pipedrive_webhook_json_data_email = ''
                    
                    # change == action , 
                if pipedrive_webhook_json_meta_action == 'change':
                    # 
                    
                    url_get_person_fields = 'https://api.pipedrive.com/v1/personFields?start=0'
                    
                    dict_custom_field_keys_response = requests.get(url = url_get_person_fields,  
                    
                    
                    ).json()
                    if dict_custom_field_keys_response['success'] != True: 
                        print(f'could not retrieve the codes for the fields of the deal, reason: {dict_custom_field_keys_response["error"]}')
                    else:
                    # 
                        fieldsDictionary = pd.DataFrame.from_dict(dict_custom_field_keys_response['data']).set_index('name')
                        # (AUTO!) ExpectedGeneratedVolume
                        # "(AUTO!) ExpectedGeneratedVolume"
                        # "Construction type"
                        
                        # "Solar panel total kW"
                        
                    
                    # key for the type of system: 
                    # 69c892392311fee6ed37c016244f8b06fc20f103
                    # key for the type of aggregate power of the system: 
                    # 2db67a52ae6eabf7817ccbac67aa136e01a405e3
                    
                    # key for the total expected volume of the system: 
                    # 69c892392311fee6ed37c016244f8b06fc20f103
                    
                    
                    # /persons/4614
                    # https://api.pipedrive.com/v1
                    # get the up-to-date values of the type of the system and the total power of the system 
                    url_get_one_person = f'https://api.pipedrive.com/v1/persons/{pipedrive_webhook_json_meta_entity_id}'
                    token = {
        'api_token': API_KEY_ADMIN_UPDATE_GENERATED_ENERGY_VOLUME
    }
                    modern_data_about_person_response = requests.get(params = token, url = url_get_one_person ).json()
                    
                    if modern_data_about_person_response['success'] != True: 
                        print(f'could not retrieve the up-to-date information about the person ')
                    else: 
                        modern_data_about_person = modern_data_about_person_response['data']
                        type_of_the_system = modern_data_about_person[fieldsDictionary.loc["Construction type", "key"]]
                        aggregate_of_the_system = modern_data_about_person[fieldsDictionary.loc["Solar panel total kW", "key"]]
                        key_expected_energy_volume = fieldsDictionary.loc["(AUTO!) ExpectedGeneratedVolume", "key"]
                    print(f'type of the system: {type_of_the_system}, the aggregate power of the system: {aggregate_of_the_system}')
                    
                    coefs_for_constr_types = { 
                        "Zeme": 1}
                    coefs_for_constr_types_dict = defaultdict(lambda x: 0.9)
                    
                    depreciative_coefficient_for_neto_system = 0.8
                    age_of_life_system = 30
                                # here could be an entire dictionary for different angles, points of compass, and months
                    generated_per_year_per_h= 1000
                    # make a parameter
                    price_per_kwh = 0.25
                    
                    total_generated_volume = depreciative_coefficient_for_neto_system* coefs_for_constr_types_dict[type_of_the_system]*generated_per_year_per_h*price_per_kwh*aggregate_of_the_system*age_of_life_system
                    print(f'The total generated volume, {total_generated_volume}')
                    
                    updated_data = {
                        "id": pipedrive_webhook_json_meta_entity_id, 
                        key_expected_energy_volume: total_generated_volume
                        
                        } 
                    
                    # update the field of the expected generated amount of energy 
                    request_update_total_generated_volume_response = requests.post(params = token, 
                    url = url_get_one_person, 
                    data = updated_data).json()
                    if request_update_total_generated_volume_response['success'] != True:
                        print(f'could not retrieve the codes for the fields of the deal, reason: {request_update_total_generated_volume_response["error"]}')
                    else:
                        print(f'deal details about economy updated successfully, ID {pipedrive_webhook_json_meta_entity_id}')
                    
                    # 
                    
                    

            new_PipedrivePerson = PipedrivePerson(
                MetaID = pipedrive_webhook_json_meta_id
                ,MetaEntity = pipedrive_webhook_json_meta_entity
                ,MetaEntityID = pipedrive_webhook_json_meta_entity_id
                ,MetaAction = pipedrive_webhook_json_meta_action
                ,MetaUserID = pipedrive_webhook_json_meta_user_id
                ,MetaCreatedDateTime = pipedrive_webhook_json_meta_timestamp
                ,OwnerID = pipedrive_webhook_json_data_owner_id
                ,PipedriveLabelPK = pipedrive_webhook_json_data_label
                ,ClientName = pipedrive_webhook_json_data_first_name
                ,ClientPhoneNumber = pipedrive_webhook_json_data_phone
                ,ClientEmail = pipedrive_webhook_json_data_email
            )
            db.session.add(new_PipedrivePerson)


        if pipedrive_webhook_json_meta_entity == 'note':
            if pipedrive_webhook_json_meta_action == 'delete':
                pipedrive_webhook_json_data_user_id = pipedrive_webhook_json_previous['user_id']
                pipedrive_webhook_json_data_deal_id = pipedrive_webhook_json_previous['deal_id']
                pipedrive_webhook_json_data_person_id = pipedrive_webhook_json_previous['person_id']
                pipedrive_webhook_json_data_content = pipedrive_webhook_json_previous['content']

            else:
                pipedrive_webhook_json_data_user_id = pipedrive_webhook_json_data['user_id']
                pipedrive_webhook_json_data_deal_id = pipedrive_webhook_json_data['deal_id']
                pipedrive_webhook_json_data_person_id = pipedrive_webhook_json_data['person_id']
                pipedrive_webhook_json_data_content = pipedrive_webhook_json_data['content']

            new_PipedriveNote = PipedriveNote(
                MetaID = pipedrive_webhook_json_meta_id
                ,MetaEntity = pipedrive_webhook_json_meta_entity
                ,MetaEntityID = pipedrive_webhook_json_meta_entity_id
                ,MetaAction = pipedrive_webhook_json_meta_action
                ,MetaUserID = pipedrive_webhook_json_meta_user_id
                ,MetaCreatedDateTime = pipedrive_webhook_json_meta_timestamp
                ,UserID = pipedrive_webhook_json_data_user_id
                ,DealID = pipedrive_webhook_json_data_deal_id
                ,PersonID = pipedrive_webhook_json_data_person_id
                ,NoteContent = pipedrive_webhook_json_data_content
            )
            db.session.add(new_PipedriveNote)


        if pipedrive_webhook_json_meta_entity == 'activity':
            if pipedrive_webhook_json_meta_action == 'delete':
                pipedrive_webhook_json_data_deal_id = pipedrive_webhook_json_previous['deal_id']
                try:
                    pipedrive_webhook_json_data_done = pipedrive_webhook_json_previous['done']
                except:
                    pipedrive_webhook_json_data_done = ''
                try:
                    pipedrive_webhook_json_data_due_date = pipedrive_webhook_json_previous['due_date']
                except:
                    pipedrive_webhook_json_data_due_date = ''
                try:
                    pipedrive_webhook_json_data_due_time = pipedrive_webhook_json_previous['due_time']['value']
                except:
                    pipedrive_webhook_json_data_due_time = ''
                try:
                    pipedrive_webhook_json_data_duration = pipedrive_webhook_json_previous['duration']['value']
                except:
                    pipedrive_webhook_json_data_duration = ''
                try:
                    pipedrive_webhook_json_data_location = pipedrive_webhook_json_previous['location']
                except:
                    pipedrive_webhook_json_data_location = ''
                pipedrive_webhook_json_data_person_id = pipedrive_webhook_json_previous['person_id']
                # public_description has been here earlier
                # if pipedrive_webhook
                try:
                    pipedrive_webhook_json_data_public_description = pipedrive_webhook_json_previous['public_description']
                except:
                    pipedrive_webhook_json_data_public_description = ''


                pipedrive_webhook_json_data_subject = pipedrive_webhook_json_previous['subject']

            else:
                pipedrive_webhook_json_data_deal_id = pipedrive_webhook_json_data['deal_id']
                try:
                    pipedrive_webhook_json_data_done = pipedrive_webhook_json_data['done']
                except:
                    pipedrive_webhook_json_data_done = ''
                try:
                    pipedrive_webhook_json_data_due_date = pipedrive_webhook_json_data['due_date']
                except:
                    pipedrive_webhook_json_data_due_date = ''
                try:
                    pipedrive_webhook_json_data_due_time = pipedrive_webhook_json_data['due_time']['value']
                except:
                    pipedrive_webhook_json_data_due_time = ''
                try:
                    pipedrive_webhook_json_data_duration = pipedrive_webhook_json_data['duration']['value']
                except:
                    pipedrive_webhook_json_data_duration = ''
                try:
                    pipedrive_webhook_json_data_location = pipedrive_webhook_json_data['location']
                except:
                    pipedrive_webhook_json_data_location = ''
                pipedrive_webhook_json_data_person_id = pipedrive_webhook_json_data['person_id']
                try:
                    pipedrive_webhook_json_data_public_description = pipedrive_webhook_json_data['public_description']
                except:
                    pipedrive_webhook_json_data_public_description = ''
                pipedrive_webhook_json_data_subject = pipedrive_webhook_json_data['subject']

            new_PipedriveActivity = PipedriveActivity(
                MetaID = pipedrive_webhook_json_meta_id
                ,MetaEntity = pipedrive_webhook_json_meta_entity
                ,MetaEntityID = pipedrive_webhook_json_meta_entity_id
                ,MetaAction = pipedrive_webhook_json_meta_action
                ,MetaUserID = pipedrive_webhook_json_meta_user_id
                ,MetaCreatedDateTime = pipedrive_webhook_json_meta_timestamp
                ,DealID = pipedrive_webhook_json_data_deal_id
                ,PersonID = pipedrive_webhook_json_data_person_id
                ,ActivityDone = pipedrive_webhook_json_data_done
                ,ActivityDueDate = pipedrive_webhook_json_data_due_date
                ,ActivityDueTime = pipedrive_webhook_json_data_due_time
                ,ActivityDuration = pipedrive_webhook_json_data_duration
                ,ActivityLocation = pipedrive_webhook_json_data_location
                ,ActivityDescription = pipedrive_webhook_json_data_public_description
                ,ActivitySubject = pipedrive_webhook_json_data_subject
                )
            db.session.add(new_PipedriveActivity)

    db.session.commit()

    return 'Webhook received!'