from django.core.management.base import BaseCommand
from baladapp.models import PoiType, Poi
import xml.etree.ElementTree as ET
import urllib2, base64


class Command(BaseCommand):
	args = '<source> <out>'
	help = ''

	def handle(self, *args, **options):
		categorie = args[0]
		out = args[1]
		try:
			username = "hackathon"
			password = "yrgm!2902"
			url = "http://w3.ftlb.be/webservice/h2o.php?tbl=xmlcomplet&cat_id=%s" % categorie

			request = urllib2.Request(url)
			base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
			request.add_header("Authorization", "Basic %s" % base64string)
			result = urllib2.urlopen(request)
			html = result.read()
			with open("%s.xml" % out, "wb") as ouf:
       				ouf.write(html)
			poiType = PoiType(
				name=out
			)
			poiType.save()
			identifiant = poiType.id
			count = 0
			tree = ET.parse("%s.xml" % out)
			root = tree.getroot()
			list = []
			for child in root:
			        for sex in child:
			                fail = 0
			                count = count + 1
			                try:
                        			titre = sex.find('titre').text
			                        lat = sex.find('localisation/localite/x').text
                        			lon = sex.find('localisation/localite/y').text
			                except:
                        			fail = 1
                			try:
			                        desc = sex.find('descriptions/description[@dat="tjr"]/texte').text
			                except:
		                        	desc = None
                			try:
                			        tel = sex.find('contacts/contact/communications/communication[@typ="tel"]/val').text
                			except:
                			        tel = None
                			if fail == 0:
                		       		list.append([titre, lat, lon, desc, tel, identifiant])

			print count, " enregistrement(s)"
			ok = 0
			for i in list:
				poi = Poi(
					name=i[0],
					latitude=i[1],
					longitude=i[2],
					description=i[3],
					phone=i[4],
					poi_type_id=i[5]
				)
				poi.save()
				ok = ok + 1
			print "%d/%d enregistrement valide" % (ok, count)
		except Exception as e:
			print e
			return
