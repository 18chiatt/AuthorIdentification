import requests
import re
import os
import time

# total download size is ~ .5GB

contributorBasePath = 'https://www.loc.gov/collections/selected-digitized-books/?fa=contributor:{' \
                      'contributor}&fo=json'
contributors = [
    {'name': 'otis,+james'},
    {'name': 'dickens,+charles'},
    {'name': 'scott,+walter'},
    {'name': 'cooper,+james+fenimore'},
    {'name': 'meade,+l.+t.'},
    {'name': 'kipling,+rudyard'},
    {'name': 'ouida'},
    {'name': 'tomlinson,+everett+t.+%28everett+titsworth%29'},
    {'name': 'douglas,+amanda+minnie'},
    {'name': 'macdonald,+george'},
    {'name': 'thackeray,+william+makepeace'},
    {'name': 'balzac,+honore+de'},
    {'name': 'hawthorne,+nathaniel'},
    {'name': 'stratemeyer,+edward'},
    {'name': 'cobb,+sylvanus'},
    {'name': 'dumas,+alexandre'},
    {'name': 'raymond,+evelyn'},
    {'name': 'southworth,+emma+dorothy+eliza+nevitte'},
    {'name': 'andersen,+h.+c.+%28hans+christian%29'},
    {'name': 'reid,+mayne'},
    {'name': 'stockton,+frank+r.'},
    {'name': 'taggart,+marion+ames'},
    {'name': 'wright,+julia+mcnair'},
    {'name': 'blanchard,+amy+ella'},
    {'name': 'chellis,+mary+dwinell'},
    {'name': 'lee+and+shepard'},
    {'name': 'carroll,+lewis'},
    {'name': 'hoffmann,+franz'},
    {'name': 'kingsley,+charles'},
    {'name': 'lytton,+edward+bulwer+lytton'},
    {'name': 'yonge,+charlotte+m.+%28charlotte+mary%29'},
    {'name': 'hope,+anthony'},
    {'name': 'oliphant,+%28margaret%29'},
    {'name': 'winter,+john+strange'},
    {'name': 'black,+william'},
    {'name': 'henty,+g.+a.+%28george+alfred%29'},
    {'name': 'rathborne,+st.+george'},
    {'name': 'sherwood,+mary+neal'},
    {'name': 'spyri,+johanna'},
    {'name': 'stevenson,+robert+louis'},
    {'name': 'brooks,+amy'},
    {'name': 'fenn,+george+manville'},
    {'name': 'hale,+edward+everett'},
    {'name': 'zola,+emile'},
    {'name': 'braddon,+m.+e.+%28mary+elizabeth%29'},
    {'name': 'craik,+dinah+maria+mulock'},
    {'name': 'garis,+howard+roger'},
    {'name': 'norris,+w.+e.+%28william+edward%29'},
    {'name': 'optic,+oliver'},
    {'name': 'ray,+anna+chapin'}
]

for contributor in contributors:
    time.sleep(2.0)
    r = requests.get(contributorBasePath.replace('{contributor}', contributor['name']))
    print(r)
    text = r.text
    linksToDocuments = re.findall('https:\\/\\/tile\\.loc\\.gov/storage-services.{1,1000}\\.txt', text)
    contributor['docLinks'] = linksToDocuments
# print(contributor)
if not os.path.exists('./data'):
    os.mkdir('./data')

for contributor in contributors:
    print(contributor['name'])
    contributorName = ''.join(ch for ch in contributor['name'] if ch.isalnum())
    print("New Name!", contributorName)

    os.mkdir('./data/' + contributorName)

    for link in contributor['docLinks']:
        fileName = link.rsplit('/')[-1]
        time.sleep(2.0)
        r = requests.get(link)
        open('./data/' + contributorName + '/' + fileName, 'wb').write(r.content)
