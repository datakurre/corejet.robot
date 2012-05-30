<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:output method="text" omit-xml-declaration="yes"/>
<xsl:strip-space elements="*"/>
<xsl:template match="//story">
*** Settings ***

Meta: Id  <xsl:value-of select="@id"/>
Meta: Title  <xsl:value-of select="@title"/>
<xsl:if test="count(given) + count(when) + count(then) > 0">

Suite Setup  Background

*** Keywords ***

<xsl:text>Background</xsl:text>
<xsl:for-each select="given">
<xsl:if test="position() &lt; 2">
    Given <xsl:value-of select="text()"/>
</xsl:if>
<xsl:if test="position() &gt; 1">
    And <xsl:value-of select="text()"/>
</xsl:if>
</xsl:for-each>
<xsl:for-each select="when">
<xsl:if test="position() &lt; 2">
    When <xsl:value-of select="text()"/>
</xsl:if>
<xsl:if test="position() &gt; 1">
    And <xsl:value-of select="text()"/>
</xsl:if>
</xsl:for-each>
<xsl:for-each select="then">
<xsl:if test="position() &lt; 2">
    Then <xsl:value-of select="text()"/>
</xsl:if>
<xsl:if test="position() &gt; 1">
    And <xsl:value-of select="text()"/>
</xsl:if>
</xsl:for-each>
</xsl:if>

*** Test Cases ***
<xsl:apply-templates select="scenario"/>
</xsl:template>
<xsl:template match="scenario">
<xsl:text>
</xsl:text>
<xsl:value-of select="@name"/>
<xsl:for-each select="given">
<xsl:if test="position() &lt; 2">
    Given <xsl:value-of select="text()"/>
</xsl:if>
<xsl:if test="position() &gt; 1">
    And <xsl:value-of select="text()"/>
</xsl:if>
</xsl:for-each>
<xsl:for-each select="when">
<xsl:if test="position() &lt; 2">
    When <xsl:value-of select="text()"/>
</xsl:if>
<xsl:if test="position() &gt; 1">
    And <xsl:value-of select="text()"/>
</xsl:if>
</xsl:for-each>
<xsl:for-each select="then">
<xsl:if test="position() &lt; 2">
    Then <xsl:value-of select="text()"/>
</xsl:if>
<xsl:if test="position() &gt; 1">
    And <xsl:value-of select="text()"/>
</xsl:if>
</xsl:for-each>
<xsl:text>
</xsl:text>
</xsl:template>
</xsl:stylesheet>
