var MODULE = (function(module){
	//module.gsearch = (module.gsearch || {})
	var moduleName = "gsearch"
	module[moduleName] = (module[moduleName] || {})
	module[moduleName].test2 = function(){
		console.log("Le module a été augmenté!")
	}

	return module
}(MODULE || {}))

var gsearch = MODULE.gsearch

gsearch.test2()
