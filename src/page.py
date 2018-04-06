from flask import render_template
from flask import url_for

class Page():
	UNSPECIFIED_TEMPLATE		= -1
	BLANK_TEMPLATE 				= 0
	REGULAR_TEMPLATE 			= 1
	CENTER_TEMPLATE 			= 2
	CENTER_AND_LEFT_TEMPLATE 	= 3
	CENTER_AND_RIGHT_TEMPLATE 	= 4
	LEFT_AND_RIGHT_TEMPLATE 	= 5

	_pageTemplateReference 		= UNSPECIFIED_TEMPLATE

	_scripts		= None		#JS scripts inserted through page.addScripts()
	_defaultJS		= None		# JS files to use by default on all pages
	_defaultCSS 	= None		#CSS files to use by default on all pages
	_userCSS		= None
	_leftColumn 	= ''
	_centerColumn	= ''
	_rightColumn	= ''
	_pageTemplate	= 'base.html'
	

	_pageTitle		= ''
	_pageContent	= ''

	
	_pageElementsCounts = 0

	def __init__(self,title):
		self.initializeVariables()
		self._pageTitle = title
		self.setDefaultScripts()


	def initializeVariables(self):
		self._scripts		= []
		self._defaultJS		= []
		self._defaultCSS	= []
		self._userCSS		= []

	def initializePageLayout(self,layoutReference):
		self._pageTemplateReference = layoutReference

	def setTemplateType(self,templateType):
		self.initializePageLayout(templateType)

	def addBlock(self, htmlBlock):
		pass

	def addBlockLeft(self, htmlBlock):
		self._leftColumn += htmlBlock

	def addBlockCenter(self, htmlBlock):
		self._centerColumn += htmlBlock

	def addBlockRight(self, htmlBlock):
		self._rightColumn += htmlBlock

	def addCSS(self,filename,blueprint):
		if(self._userCSS is None):
			self._userCSS = []

		self.addStaticUrlToList(self._userCSS,"css/"+filename,blueprint)

	def setDefaultScripts(self):
		self.addDefaultScript('jquery-3.2.1.min.js')
		self.addDefaultScript('bootstrap.min.js')
		self.addDefaultScript('vue.js')
		

	def addScript(self, scriptLocalPath, blueprint=None):

		self.addStaticUrlToList(self._scripts,"js/"+scriptLocalPath,blueprint)
		
	def addDefaultScript(self, scriptLocalPath, blueprint=None):
		if(self._defaultJS is None):
			self._defaultJS = []
		print("add default script : "+scriptLocalPath)
		self.addStaticUrlToList(self._defaultJS,"js/"+scriptLocalPath,blueprint)

		print(" ".join(self._defaultJS))


	def addStaticUrlToList(self, urlList, filename,blueprint=None):
		if(blueprint is not None):
			blueprint+='.'
		else :
			blueprint = ''

		if(urlList is None):
			urlList = []

		urlList.append(
			url_for("{blueprint}static".format(blueprint=blueprint),
					filename=filename)
		)


	def setTitle(self,title):
		self._pageTitle = title

	def setContent(self, content):
		self._pageContent = content

	def initializeTemplateIfNotSpecified(self):
		if(self._pageTemplateReference != self.UNSPECIFIED_TEMPLATE):
			return

		regularTemplate = self._centerColumn and self._leftColumn and self._rightColumn
		centerTemplate  = self._centerColumn and (not self._leftColumn) and (not self._rightColumn)
		leftAndRightTemplate = (not self._centerColumn) and self._leftColumn and self._rightColumn
		centerAndRightTemplate = (not self._leftColumn) and self._centerColumn and self._rightColumn
		centerAndLeftTemplate = (not self._rightColumn) and self._centerColumn and self._leftColumn

		if(regularTemplate):
			self.initializePageLayout(self.REGULAR_TEMPLATE)
		elif(centerTemplate):
			self.initializePageLayout(self.CENTER_TEMPLATE)
		elif(leftAndRightTemplate):
			self.initializePageLayout(self.LEFT_AND_RIGHT_TEMPLATE)
		elif(centerAndRightTemplate):
			self.initializePageLayout(self.CENTER_AND_RIGHT_TEMPLATE)
		elif(centerAndLeftTemplate):
			self.initializePageLayout(self.CENTER_AND_LEFT_TEMPLATE)
		else:
			self.initializePageLayout(self.CENTER_TEMPLATE)

	def generatePageContent(self):
		pagePartsList = []

		if(self._pageTemplateReference == self.CENTER_TEMPLATE):
			pagePartsList.append(self._centerColumn)
		elif(self._pageTemplateReference == self.REGULAR_TEMPLATE):
			pagePartsList.append(self.includeContentInTag(self._leftColumn,"col-md-2"))
			pagePartsList.append(self.includeContentInTag(self._centerColumn,"col-md-8"))
			pagePartsList.append(self.includeContentInTag(self._rightColumn,"col-md-2"))
		elif(self._pageTemplateReference == self.LEFT_AND_RIGHT_TEMPLATE):
			pagePartsList.append(self.includeContentInTag(self._leftColumn,"col-md-4"))
			pagePartsList.append(self.includeContentInTag(self._rightColumn,"col-md-4"))
		elif(self._pageTemplateReference == self.CENTER_AND_RIGHT_TEMPLATE):
			pagePartsList.append(self.includeContentInTag(self._centerColumn,"col-md-8"))
			pagePartsList.append(self.includeContentInTag(self._rightColumn,"col-md-4"))
		elif(self._pageTemplateReference == self.CENTER_AND_LEFT_TEMPLATE):
			pagePartsList.append(self.includeContentInTag(self._leftColumn,"col-md-4"))
			pagePartsList.append(self.includeContentInTag(self._centerColumn,"col-md-8"))
		else:
			raise NameError("Unknown page template : {template}".format(template=self._pageTemplateReference))

		divClass="row"
		rowContent = "\r\n".join(pagePartsList)

		return self.includeContentInTag(rowContent,divClass,"div")

	def initializeDefaultScripts(self):
		pass

	def includeContentInTag(self,content,elementClass="",tag="div"):
		return "<{tag} class='{elementClass}'>{content}</{tag}>".format(tag=tag,elementClass=elementClass,content=content)

	def generateUserScripts(self):

		return self.generateScriptTags(self._scripts)

	def generateDefaultScripts(self):
		
		return self.generateScriptTags(self._defaultJS)

	def generateScriptTags(self,scriptList):
		scriptTags = ''

		if (scriptList is None):
			scriptList = []

		for script in scriptList:
			scriptTags += "<script src='{url}' type='text/javascript'></script>\r\n".format(url=script)

		print("script Tags = ")
		print(scriptTags)
		return scriptTags

	def generateCssTags(self):
		cssTags = ''

		if(self._defaultCSS is None):
			self._defaultCSS = []

		if(self._userCSS is None):
			self._userCSS = []

		cssList = self._defaultCSS + self._userCSS

		for css in cssList:
			cssTags += "<link rel='stylesheet' href='{css}'/>\r\n".format(css=css)

		return cssTags


	def render(self):
		self.initializeTemplateIfNotSpecified()
		self._pageContent 		= self.generatePageContent()
		defaultScripts 			= self.generateDefaultScripts()
		scripts 				= self.generateUserScripts()
		css 					= self.generateCssTags()
		print(css+"COUCOU")
		#self.loadDefaultStaticFiles()

		return render_template(self._pageTemplate, 
								context={
									'title': self._pageTitle, 
									'content': self._pageContent,
									'css': css,
									'headerJS': defaultScripts,
									'scriptsBottom': scripts
									}
								)

	def next_id(self):
		self._pageElementsCounts = self._pageElementsCounts +1
		return self._pageElementsCounts