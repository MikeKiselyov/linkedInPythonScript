import requests
import json
import time

headers = {
    'sec-fetch-mode': 'cors',
    'dnt': '1',
    'accept-encoding': 'gzip, deflate, br',
    'x-li-lang': 'ru_RU',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'bcookie="v=2&ac39d8ad-3cfb-41ec-856a-0bc60d3ec2ac"; bscookie="v=1&20190510125749ac18b2d1-ae9f-4d0c-812c-e1c45bdf2f68AQG9Ro8Z5jghxbgYyOgri0SQRt2NNUfR"; _ga=GA1.2.727299436.1557493070; aam_uuid=31355844993612041240310717160185273691; li_sugr=275a0b9e-1880-406b-908f-4b3928f11390; lissc2=1; li_oatml=AQFbtpuIyzhBNAAAAWzOv14BZHE4t1S5rPcIYT5CGZScVxjTxTZbkoofXm7vak_mvqjjtoOD0kphdKCeLxCR45X5H4ecUBSQ; _guid=1ca03b1c-23c1-446c-b4c2-587dcf6d490e; _lipt=CwEAAAFtWFKVqEodsnOV8rY_qQMMcdLKxihNF0ocZOSmPsC3jyP1-zJfkhTpSpbQoFrqGrbW-VhkJR4chgrQsGbuJcwTXxZtkplJWuRb7Zjx1H0lhfkJltCnCmuZITvqXFog6yM8RB3jGeN1ILaCTFXJ9seC5Qh8QfMfHAg69j4SbzcPlEtESjkj5kvf-thJQPmafKmonL3825-W8IL2yHyq7bsy6QrsqP9841lAKwhxxkvXnh6FmPTEfn7CQ9DRASrSYurmrbMPoLNCqsM0eoF3_v-_j6aF0xS_Ka12d51IvKiieQqEARaz4HhYmQVclJWUihDUfvS3SXNkZW9SGxcMKs1m0rJycZdvDKoOI81AgeMFUfTt; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-1303530583%7CMCIDTS%7C18162%7CMCMID%7C31201438012785101670324484164403654288%7CMCAAMLH-1569749672%7C6%7CMCAAMB-1569749672%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1569152072s%7CNONE%7CvVersion%7C3.3.0%7CMCCIDH%7C-86850748; SID=bea14049-38c9-4c68-8abb-909554626f11; VID=V_2019_09_22_09_2156348; visit=v=1&M; JSESSIONID="ajax:3037872120626961424"; lissc1=1; li_at=AQEDASTfrf4A7qllAAABbVhgS80AAAFtfGzPzU0AS6xjK_fE1-I9xUl9pEDfaYa9W84VnYtSdKg5s3P5V4oDeMs_fN44D1Dnu0HEAJcMBkzymZSld7p2qHmf1uDQg3iIowMwfWs7vIjb6HO1NH6xwV45; liap=true; sl=v=1&Fe4OD; lang=v=2&lang=ru-ru; lidc="b=OB46:g=1980:u=388:i=1569145810:t=1569217778:s=AQHj-2czlC-u-vmxu3Lx23GFjAvaG7n1"; UserMatchHistory=AQI0EahLX5ZvoQAAAW1YYPBmd_ceBaxsYsXCkVjsGnHZblsefYUYtHNnCnMBh-m55gTWVi6zpiUlcVlLxB5bWPABuK5rhtxXh-fVbzvdgjnMZg0EDJpBCzpyOrGxeuzA3goQvJkmzz_Ogd1bKAfcu7r2sQnvi6TFputbv0Kn2DQPcGnN91MxUXFPZ3MbohcQs-k2nQ',
    'x-restli-protocol-version': '2.0.0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'x-li-page-instance': 'urn:li:page:d_flagship3_search_srp_top;sqJ8k36mTtqlTfX1cxsjdQ==',
    'accept': 'application/vnd.linkedin.normalized+json+2.1',
    'csrf-token': 'ajax:3037872120626961424',
    'x-li-track': '{"clientVersion":"1.5.*","osName":"web","timezoneOffset":3,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
    'authority': 'www.linkedin.com',
    'referer': 'https://www.linkedin.com/search/results/all/?authorCompany=%5B%5D&authorIndustry=%5B%5D&contactInterest=%5B%5D&facetCity=%5B%5D&facetCompany=%5B%5D&facetConnectionOf=%5B%5D&facetCurrentCompany=%5B%5D&facetCurrentFunction=%5B%5D&facetGeoRegion=%5B%5D&facetGroup=%5B%5D&facetGuides=%5B%5D&facetIndustry=%5B%5D&facetNetwork=%5B%5D&facetNonprofitInterest=%5B%5D&facetPastCompany=%5B%5D&facetProfessionalEvent=%5B%5D&facetProfileLanguage=%5B%5D&facetRegion=%5B%5D&facetSchool=%5B%5D&facetSeniority=%5B%5D&facetServiceCategory=%5B%5D&facetState=%5B%5D&groups=%5B%5D&keywords=HR&origin=GLOBAL_SEARCH_HEADER&page=1&refresh=false&skillExplicit=%5B%5D&topic=%5B%5D',
    'sec-fetch-site': 'same-origin'
}

params = (
    ('count', '40'),
    ('filters', 'List(geoRegion->by:0,resultType->PEOPLE)'),
    ('keywords', 'HR'),
    ('origin', 'GLOBAL_SEARCH_HEADER'),
    ('q', 'all'),
    ('queryContext', 'List(spellCorrectionEnabled->true,relatedSearchesEnabled->true)'),
    ('start', '700')
)

response = requests.get('https://www.linkedin.com/voyager/api/search/blended', headers=headers, params=params)
response_users = response.json()['data']['elements'][0]['elements']
lenght_users = len(response_users)
print(f'Count users: {lenght_users}')

names = {}
for i in range(len(response_users)):
    znakom = str(response_users[i]['memberDistance']['value'])
    if znakom == 'DISTANCE_2':
        names[response_users[i]['trackingId']] = response_users[i]['publicIdentifier']
print(names)

headers_2 = {
    'sec-fetch-mode': 'cors',
    'origin': 'https://www.linkedin.com',
    'accept-encoding': 'gzip, deflate, br',
    'x-li-lang': 'ru_RU',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'bcookie="v=2&ac39d8ad-3cfb-41ec-856a-0bc60d3ec2ac"; bscookie="v=1&20190510125749ac18b2d1-ae9f-4d0c-812c-e1c45bdf2f68AQG9Ro8Z5jghxbgYyOgri0SQRt2NNUfR"; _ga=GA1.2.727299436.1557493070; aam_uuid=31355844993612041240310717160185273691; li_sugr=275a0b9e-1880-406b-908f-4b3928f11390; lissc2=1; li_oatml=AQFbtpuIyzhBNAAAAWzOv14BZHE4t1S5rPcIYT5CGZScVxjTxTZbkoofXm7vak_mvqjjtoOD0kphdKCeLxCR45X5H4ecUBSQ; _guid=1ca03b1c-23c1-446c-b4c2-587dcf6d490e; _lipt=CwEAAAFtWFKVqEodsnOV8rY_qQMMcdLKxihNF0ocZOSmPsC3jyP1-zJfkhTpSpbQoFrqGrbW-VhkJR4chgrQsGbuJcwTXxZtkplJWuRb7Zjx1H0lhfkJltCnCmuZITvqXFog6yM8RB3jGeN1ILaCTFXJ9seC5Qh8QfMfHAg69j4SbzcPlEtESjkj5kvf-thJQPmafKmonL3825-W8IL2yHyq7bsy6QrsqP9841lAKwhxxkvXnh6FmPTEfn7CQ9DRASrSYurmrbMPoLNCqsM0eoF3_v-_j6aF0xS_Ka12d51IvKiieQqEARaz4HhYmQVclJWUihDUfvS3SXNkZW9SGxcMKs1m0rJycZdvDKoOI81AgeMFUfTt; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-1303530583%7CMCIDTS%7C18162%7CMCMID%7C31201438012785101670324484164403654288%7CMCAAMLH-1569749672%7C6%7CMCAAMB-1569749672%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1569152072s%7CNONE%7CvVersion%7C3.3.0%7CMCCIDH%7C-86850748; SID=bea14049-38c9-4c68-8abb-909554626f11; VID=V_2019_09_22_09_2156348; visit=v=1&M; JSESSIONID="ajax:3037872120626961424"; lissc1=1; li_at=AQEDASTfrf4A7qllAAABbVhgS80AAAFtfGzPzU0AS6xjK_fE1-I9xUl9pEDfaYa9W84VnYtSdKg5s3P5V4oDeMs_fN44D1Dnu0HEAJcMBkzymZSld7p2qHmf1uDQg3iIowMwfWs7vIjb6HO1NH6xwV45; liap=true; sl=v=1&Fe4OD; lang=v=2&lang=ru-ru; lidc="b=OB46:g=1980:u=388:i=1569145810:t=1569217778:s=AQHj-2czlC-u-vmxu3Lx23GFjAvaG7n1"; UserMatchHistory=AQI0EahLX5ZvoQAAAW1YYPBmd_ceBaxsYsXCkVjsGnHZblsefYUYtHNnCnMBh-m55gTWVi6zpiUlcVlLxB5bWPABuK5rhtxXh-fVbzvdgjnMZg0EDJpBCzpyOrGxeuzA3goQvJkmzz_Ogd1bKAfcu7r2sQnvi6TFputbv0Kn2DQPcGnN91MxUXFPZ3MbohcQs-k2nQ',
    'x-restli-protocol-version': '2.0.0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'x-li-page-instance': 'urn:li:page:d_flagship3_search_srp_top;ZAO7tKABRDSoinThFpMXPA==',
    'content-type': 'application/json; charset=UTF-8',
    'accept': 'application/vnd.linkedin.normalized+json+2.1',
    'csrf-token': 'ajax:3037872120626961424',
    'x-li-track': '{"clientVersion":"1.5.*","osName":"web","timezoneOffset":3,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
    'authority': 'www.linkedin.com',
    'referer': 'https://www.linkedin.com/search/results/all/?keywords=HR&origin=GLOBAL_SEARCH_HEADER&page=100',
    'sec-fetch-site': 'same-origin',
    'dnt': '1'
}

for i in names:
    data_2 = '{"emberEntityName":"growth/invitation/norm-invitation","invitee":{"com.linkedin.voyager.growth.invitation.InviteeProfile":{"profileId":"anastasia-burakova-96127486"}},"trackingId":"hjbLqPPLSsKQwFNQoqw63A=="}'
    json_dict = json.loads(data_2)
    json_dict['invitee']['com.linkedin.voyager.growth.invitation.InviteeProfile']['profileId'] = names[i]
    json_dict['trackingId'] = i
    updated_invite = json.dumps(json_dict, indent=4)
    response = requests.post('https://www.linkedin.com/voyager/api/growth/normInvitations', headers=headers_2,
                             data=updated_invite)
    print(response.status_code)
    print('_______________________________________________________')
    while str(response.status_code) == '429':
        time.sleep(300)
