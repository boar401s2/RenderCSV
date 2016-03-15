from web import template
import web
from model.holeparser import HoleParser
from config import CSV_PATH

class index:
    def GET(self):
        self.holeParser = HoleParser(CSV_PATH)
        self.holeParser.parse()
        render = template.render('pages/')
        scale = 10

        return render.index(self.holeParser.getEastingDifference()*scale, self.holeParser.getNorthingDifference()*scale,
                            self.holeParser.normalizePointCloud(self.holeParser.getMinEasting().easting, self.holeParser.getMinNorthing().northing, 0, scale=10,),
                            40)
        #return "Hello World!"