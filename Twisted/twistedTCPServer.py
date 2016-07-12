#! /usr/local/bin/python
#! coding=utf-8

import twisted
from twisted.web import resource, server
from twisted.internet import reactor
from twisted.enterprise import adbapi


class BlobLoads(resource.Resource):
    def __init__(self, dbconn):
        self.dbconn = dbconn
        resource.Resource.__init__(self)
    def _getBlobs(self, txn, query):
        txn.execute(query)
        return txn.fetchall()
    def render_GET(self, request):
        query = "select id, blobdoc from blob_tab"
        self.dbconn.runInteraction(self._getBlobs, query).addCallback(
                self._writeBlobs, request).addErrback(
                    self._exception, request)
        return server.NOT_DONE_YET
    def _writeBlobs(self, results, request):
        request.write("""
        <html>
        <head><title>BLOBs manipulating</title></head>
        <body>
        <h2>Writing BLOBs from the database to your disk</h2>
         """)
        for id, blobdoc in results:
            request.write("<i>/tmp/picture%s.bmp</i><br/>" % id)
            blob = blobdoc.read()
            output = open("/tmp/picture%s.bmp" % id, 'wb')
            output.write(blob)
            output.close()

        request.write("""
        <p>Operation completed</p>
        </body>
        </html>
        """)
        request.finish( )
    def _exception(self, error, request):
        request.write("Error obtaining BLOBs: %s" % error.getErrorMessage())
        request.write("""
                <p>Could not complete operation</p>
                </body>
                </html>
                """)
        request.finish( )

class SiteResource(resource.Resource):
    def __init__(self, dbconn):
        resource.Resource.__init__(self)
        self.putChild('', BlobLoads(dbconn))


if __name__ == "__main__":
    dbconn = adbapi.ConnectionPool('MySQLdb', user='root', password ='123456', dsn='192.168.1.46/TestDB')
    site = server.Site(SiteResource(dbconn))
    print "Listening on port 8000"
    reactor.listenTCP(8000, site)
    reactor.run()
