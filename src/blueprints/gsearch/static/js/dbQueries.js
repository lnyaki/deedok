var MODULE = (function(module,$,moduleName){
	
	var localModule = (module[moduleName] || {})

	localModule.test = function(){
		console.log("ça marche")
	}

	module[moduleName] = localModule
	return module
}(    (MODULE || {}),$, "gsearch"))


var gsearch = MODULE.gsearch

gsearch.test()


console.log(MODULE)