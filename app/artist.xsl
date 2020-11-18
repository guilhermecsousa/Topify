<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/lfm">
        <html>
            <body>
                <table>    
                    <tr>
                        <xsl:for-each select="/lfm/artist/similar/artist" >
                            <td>
                                <xsl:value-of select="name"/>
                                 <xsl:text> , </xsl:text>
                            </td>
                        </xsl:for-each>
                    </tr>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
