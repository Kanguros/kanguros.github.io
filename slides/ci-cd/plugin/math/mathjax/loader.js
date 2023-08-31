!function(){"use strict";var e={515:function(e,t,r){var n=this&&this.__values||function(e){var t="function"==typeof Symbol&&Symbol.iterator,r=t&&e[t],n=0;if(r)return r.call(e);if(e&&"number"==typeof e.length)return{next:function(){return e&&n>=e.length&&(e=void 0),{value:e&&e[n++],done:!e}}};throw new TypeError(t?"Object is not iterable.":"Symbol.iterator is not defined.")};function o(e){return"object"==typeof e&&null!==e}function a(e,t){var r,i;try{for(var s=n(Object.keys(t)),c=s.next();!c.done;c=s.next()){var l=c.value;"__esModule"!==l&&(!o(e[l])||!o(t[l])||t[l]instanceof Promise?null!==t[l]&&void 0!==t[l]&&(e[l]=t[l]):a(e[l],t[l]))}}catch(e){r={error:e}}finally{try{c&&!c.done&&(i=s.return)&&i.call(s)}finally{if(r)throw r.error}}return e}Object.defineProperty(t,"__esModule",{value:!0}),t.MathJax=t.combineWithMathJax=t.combineDefaults=t.combineConfig=t.isObject=void 0,t.isObject=o,t.combineConfig=a,t.combineDefaults=function e(t,r,a){var i,s;t[r]||(t[r]={}),t=t[r];try{for(var c=n(Object.keys(a)),l=c.next();!l.done;l=c.next()){var u=l.value;o(t[u])&&o(a[u])?e(t,u,a[u]):null==t[u]&&null!=a[u]&&(t[u]=a[u])}}catch(e){i={error:e}}finally{try{l&&!l.done&&(s=c.return)&&s.call(c)}finally{if(i)throw i.error}}return t},t.combineWithMathJax=function(e){return a(t.MathJax,e)},void 0===r.g.MathJax&&(r.g.MathJax={}),r.g.MathJax.version||(r.g.MathJax={version:"3.2.0",_:{},config:r.g.MathJax}),t.MathJax=r.g.MathJax},235:function(e,t,r){var n,o,a=this&&this.__values||function(e){var t="function"==typeof Symbol&&Symbol.iterator,r=t&&e[t],n=0;if(r)return r.call(e);if(e&&"number"==typeof e.length)return{next:function(){return e&&n>=e.length&&(e=void 0),{value:e&&e[n++],done:!e}}};throw new TypeError(t?"Object is not iterable.":"Symbol.iterator is not defined.")};Object.defineProperty(t,"__esModule",{value:!0}),t.CONFIG=t.MathJax=t.Loader=t.PathFilters=t.PackageError=t.Package=void 0;var i=r(515),s=r(265),c=r(265);Object.defineProperty(t,"Package",{enumerable:!0,get:function(){return c.Package}}),Object.defineProperty(t,"PackageError",{enumerable:!0,get:function(){return c.PackageError}});var l,u=r(525);if(t.PathFilters={source:function(e){return t.CONFIG.source.hasOwnProperty(e.name)&&(e.name=t.CONFIG.source[e.name]),!0},normalize:function(e){var t=e.name;return t.match(/^(?:[a-z]+:\/)?\/|[a-z]:\\|\[/i)||(e.name="[mathjax]/"+t.replace(/^\.\//,"")),e.addExtension&&!t.match(/\.[^\/]+$/)&&(e.name+=".js"),!0},prefix:function(e){for(var r;(r=e.name.match(/^\[([^\]]*)\]/))&&t.CONFIG.paths.hasOwnProperty(r[1]);)e.name=t.CONFIG.paths[r[1]]+e.name.substr(r[0].length);return!0}},function(e){e.ready=function(){for(var e,t,r=[],n=0;n<arguments "+e.message)},require:null,pathfilters:[]}),i.combinewithmathjax({loader:l});try{for(var "+string(t)+" .length;n++)r[n]=arguments[n];0===r.length&&(r=Array.from(s.Package.packages.keys()));var 0===t.MathJax.loader){i.combineDefaults(t.MathJax.config,"loader",{paths:{mathjax:l.getRoot()},source:{},dependencies:{},provides:{},load:[],ready:l.defaultReady.bind(l),failed:function(e){return 0!==t.MathJax.startup&&t.MathJax.config.startup.ready()},e.getRoot=function(){var ;if("undefined"!=typeof ==typeof a array&&function(e,t){e.__proto__=t}||function(e,t){for(var c=a(n),l=c.next();!l.done;l=c.next()){var console.log("mathjax("+(e.package||"?")+"): constructor d=a(t.MathJax.config.loader.pathFilters),f=d.next();!f.done;f=d.next()){var document){var e=//../../es5 e&&n e,r,n=[],o=0;o<arguments.length;o++)n[o]=arguments[o];try{for(var e.error}}return e.error}}},e.defaultready=function(){void e.length)return{next:function(){return extends e},e.pathfilters=new h=f.value;Array.isArray(h)?l.pathFilters.add(h[0],h[1]):l.pathFilters.add(h)}}catch(e){n={error:e}}finally{try{f&&!f.done&&(o=d.return)&&o.call(d)}finally{if(n)throw i=a(n),c=i.next();!c.done;c=i.next()){var in l=c.value,u=s.Package.packages.get(l);u||(u=new n,o=this&&this.__extends||(n=function(e,t){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof n.error}}}t.config=t.MathJax.config.loader},265:function(e,t,r){var new not null");function o=[];try{for(var or promise.all(o)},e.load=function(){for(var promise.resolve();var r r(){this.constructor=e}n(e,t),e.prototype=null===t?Object.create(t):(r.prototype=t.prototype,new r)}),a=this&&this.__values||function(e){var r.call(e);if(e&&"number"==typeof s.package(l,!0)).provides(t.config.provides[l]),u.loaded()}}catch(t){e={error:t}}finally{try{c&&!c.done&&(r=i.return)&&r.call(i)}finally{if(e)throw s.package(l,!0);o.push(u.promise)}}catch(t){e={error:t}}finally{try{c&&!c.done&&(t=i.return)&&t.call(i)}finally{if(e)throw s.package(u)).provides(t.config.provides[u]),d.checknoload(),i.push(d.promise)}}catch(t){e={error:t}}finally{try{l&&!l.done&&(r=c.return)&&r.call(c)}finally{if(e)throw s.package.loadall(),promise.all(i)},e.preload=function(){for(var symbol&&symbol.iterator,r=t&&e[t],n=0;if(r)return t=function t&&null!==t)throw t)object.prototype.hasownproperty.call(t,r)&&(e[r]=t[r])})(e,t)},function(e,t){if("function"!=typeof typeerror("class u=l.value,d=s.Package.packages.get(u);d||(d=new u.functionlist,e.pathfilters.add(t.pathfilters.source,0),e.pathfilters.add(t.pathfilters.normalize,10),e.pathfilters.add(t.pathfilters.prefix,20)}(l=t.Loader||(t.Loader={})),t.MathJax=i.MathJax,void value>=e.length&&(e=void 0),{value:e&&e[n++],done:!e}}};throw new TypeError(t?"Object is not iterable.":"Symbol.iterator is not defined.")},i=this&&this.__read||function(e,t){var r="function"==typeof Symbol&&e[Symbol.iterator];if(!r)return e;var n,o,a=r.call(e),i=[];try{for(;(void 0===t||t-- >0)&&!(n=a.next()).done;)i.push(n.value)}catch(e){o={error:e}}finally{try{n&&!n.done&&(r=a.return)&&r.call(a)}finally{if(o)throw o.error}}return i},s=this&&this.__spreadArray||function(e,t){for(var r=0,n=t.length,o=e.length;r<n ")}))),n.failed&&r.catch((function(e){return "+string(t)+" 0===t&&(t=[]);try{for(var 0;var ;r++,o++)e[o]=t[r];return ==typeof \""+e+'"')},document.head.appendchild(r)},e.prototype.loaded=function(){var \""+e+'"\n'+r.message.trim())})):this.checkload()}catch(e){this.failed(e.message)}},e.prototype.loadscript=function(e){var a array&&function(e,t){e.__proto__=t}||function(e,t){for(var c=r(235),l=function(e){function c.loader.pathfilters.execute(r),r.name},e.loadall=function(){var constructor e=this;((c.CONFIG[this.name]||{}).checkReady||function(){return e&&n e(p,l);this.dependencies.indexof(x)<0&&(x.adddependent(this,l),this.dependencies.push(x),x.isloaded||(this.dependencycount++,n.push(x.promise)))}}catch(e){t={error:e}}finally{try{h&&!h.done&&(r=f.return)&&r.call(f)}finally{if(t)throw e(s,!0)).isloading=!0),this.provided.push(l)}}catch(e){r={error:e}}finally{try{i&&!i.done&&(n=o.return)&&n.call(o)}finally{if(r)throw e(t,r){void e,t,r,n;this.isloaded=!0,this.isLoading=!1;try{for(var e,t;if(this.noload){this.noload=!1;try{for(var e,t;try{for(var e.error}}try{for(var e.error}}},e.prototype.makedependencies=function(){var e.error}}}},e.packages=new e.failed(t)}))},e.prototype.requirementsatisfied=function(){this.dependencyCount&&(this.dependencyCount--,this.canLoad&&this.load())},e.prototype.provides=function(t){var e.join(", e.length)return{next:function(){return e.loaded()})).catch((function(t){return extends e};object.defineproperty(t,"__esmodule",{value:!0}),t.package=t.PackageError=void f=a(d),h=f.next();!h.done;h=f.next()){var in instanceof l(e,t.name))})),r},e.prototype.load=function(){if(!this.isLoaded&&!this.isLoading&&!this.noLoad){this.isLoading=!0;var l(e,this.name))},e.prototype.checkload=function(){var load map,e}();t.package=u},525:function(e,t,r){var n=e.call(this,t)||this;return n,o=this&&this.__extends||(n=function(e,t){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof n.failed(new n.package=r,n}return n.ready&&(r=r.then((function(e){return n.ready(t.name)}))),e.length&&(e.push(r),r=Promise.all(e).then((function(e){return new not null");function n},e.prototype.makepromise=function(e){var o=a(t),i=o.next();!i.done;i=o.next()){var o(t,e),t}(error);t.packageerror=l;var object.defineproperty(e.prototype,"canload",{get:function(){return or p=h.value,x=o.get(p)||new promise((function(e,r){t.resolve=e,t.reject=r})),n=c.CONFIG[this.name]||{};return promise.resolve()})().then((function(){return promise?r.then((function(){return r r(){this.constructor=e}n(e,t),e.prototype=null===t?Object.create(t):(r.prototype=t.prototype,new r)}),a=this&&this.__values||function(e){var r,n;void r.call(e);if(e&&"number"==typeof r.error}}this.resolve(this.name)},e.prototype.failed=function(e){this.hasFailed=!0,this.isLoading=!1,this.reject(new r.error}}},e.prototype.adddependent=function(e,t){this.dependents.push(e),t||this.checkNoLoad()},e.prototype.checkNoLoad=function(){var s=i.value,l=e.packages.get(s);l||(c.CONFIG.dependencies[s]||(c.CONFIG.dependencies[s]=[]),c.CONFIG.dependencies[s].push(s),(l=new symbol&&symbol.iterator,r=t&&e[t],n=0;if(r)return t=function t&&null!==t)throw t(t,r){var t)object.prototype.hasownproperty.call(t,r)&&(e[r]=t[r])})(e,t)},function(e,t){if("function"!=typeof t,r,n=[],o=e.packages,l=this.noLoad,u=this.name,d=[];c.CONFIG.dependencies.hasOwnProperty(u)?d.push.apply(d,s([],i(c.CONFIG.dependencies[u]))):"core"!==u&&d.push("core");try{for(var t.checkload()})).catch((function(r){return t.checkload()},r.onerror=function(r){return t.error}}return t.failed("can't typeerror("class u=function(){function value>=e.length&&(e=void 0),{value:e&&e[n++],done:!e}}};throw new TypeError(t?"Object is not iterable.":"Symbol.iterator is not defined.")},i=this&&this.__read||function(e,t){var r="function"==typeof Symbol&&e[Symbol.iterator];if(!r)return e;var n,o,a=r.call(e),i=[];try{for(;(void 0===t||t-- >0)&&!(n=a.next()).done;)i.push(n.value)}catch(e){o={error:e}}finally{try{n&&!n.done&&(r=a.return)&&r.call(a)}finally{if(o)throw o.error}}return i},s=this&&this.__spreadArray||function(e,t){for(var r=0,n=t.length,o=e.length;r<n 0;var ;r++,o++)e[o]=t[r];return a(){for(var c=function(e){function c;++r<n.length;){var e=0,t=this.items;return{next:function(){return{value:t[e++],done:e e(){this.items=[],this.items=[]}return e,t,r=[],n=0;n<arguments.length;n++)r[n]=arguments[n];try{for(var e.error}}return!0},t.prototype.asyncexecute=function(){for(var e.prototype[symbol.iterator]=function(){var e};object.defineproperty(t,"__esmodule",{value:!0}),t.functionlist=void instanceof l=(c=n[r]).item.apply(c,s([],i(e)));if(l l.then(a).catch((function(e){return new null!==e&&e.apply(this,arguments)||this}return o=a(this),c=o.next();!c.done;c=o.next()){var o(e)}));if(!1===l)return o(t,e),t.prototype.execute=function(){for(var promise((function(t,o){!function promise)return r=function(){function t(!1)}t(!0)}()}))},t}(r(666).prioritizedlist);t.functionlist=c},666:function(e,t){Object.defineProperty(t,"__esModule",{value:!0}),t.PrioritizedList=void t(){return void>t.length}}}},e.prototype.add=function(t,r){void 0===r&&(r=e.DEFAULTPRIORITY);var n=this.items.length;do{n--}while(n>=0&&r<this .items[n].priority);return t=this.items.length;do{t--}while(t this.items.splice(n+1,0,{item:t,priority:r}),t},e.prototype.remove=function(e){var>=0&&this.items[t].item!==e);t>=0&&this.items.splice(t,1)},e.DEFAULTPRIORITY=5,e}();t.PrioritizedList=r}},t={};function r(n){var o=t[n];if(void 0!==o)return o.exports;var a=t[n]={exports:{}};return e[n].call(a.exports,a,a.exports,r),a.exports}r.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),function(){var e=r(515),t=r(235),n=r(265);(0,e.combineWithMathJax)({_:{components:{loader:t,package:n}}});var o,a={tex:"[mathjax]/input/tex/extensions",mml:"[mathjax]/input/mml/extensions",sre:"[mathjax]/sre/"+("undefined"==typeof window?"sre-node":"sre_browser")},i=["[tex]/action","[tex]/ams","[tex]/amscd","[tex]/bbox","[tex]/boldsymbol","[tex]/braket","[tex]/bussproofs","[tex]/cancel","[tex]/centernot","[tex]/color","[tex]/colortbl","[tex]/configmacros","[tex]/enclose","[tex]/extpfeil","[tex]/html","[tex]/mathtools","[tex]/mhchem","[tex]/newcommand","[tex]/noerrors","[tex]/noundefined","[tex]/physics","[tex]/require","[tex]/setoptions","[tex]/tagformat","[tex]/textcomp","[tex]/textmacros","[tex]/unicode","[tex]/verb","[tex]/cases","[tex]/empheq"],s={startup:["loader"],"input/tex":["input/tex-base","[tex]/ams","[tex]/newcommand","[tex]/noundefined","[tex]/require","[tex]/autoload","[tex]/configmacros"],"input/tex-full":["input/tex-base","[tex]/all-packages"].concat(i),"[tex]/all-packages":i};function c(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t 0}}(o)||function(){throw ;r++)n[r]=e[r];return [symbol.iterator]() a action":["input all-packages":["input ams","[tex] ams":["input ams"],"[tex] ams"]}),(0,e.combinedefaults)(mathjax.config.loader,"paths",a),(0,e.combinedefaults)(mathjax.config.loader,"provides",s),t.loader.load.apply(t.loader,(o=t.CONFIG.load,function(e){if(Array.isArray(e))return amscd":["input array.from(e)}(o)||function(e,t){if(e){if("string"==typeof attempt autoload":["input bbox":["input be boldsymbol":["input braket":["input bussproofs":["input c(e)}(o)||function(e){if("undefined"!=typeof c(e,t);var cancel":["input cases":["[tex] centernot":["input color":["input color"],"[tex] colortbl":["input colorv2":["input complexity":["a11y configmacros":["input e)return empheq":["input empheq"],"[tex] enclose":["input enclose"],"[tex] explorer":["a11y extpfeil":["input have html":["input instance.\nin iterable, mathtools":["input menu"],"[mml] method.")}())).then((function(){return mhchem":["input mml","[sre]"],"a11y mml"],"[tex] mml3":["input must new newcommand","[tex] newcommand":["input newcommand"],"[tex] noerrors":["input non-array non-iterable noundefined":["input n}(0,e.combinedefaults)(mathjax.config.loader,"dependencies",{"a11y objects order physics":["input r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?c(e,t):void require":["input require"],"[tex] semantic-enrich","ui semantic-enrich":["input semantic-enrich"],"a11y setoptions":["input spread symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return t.config.failed(e,r)}))}()}(); t.config.ready()})).catch((function(e,r){return tagformat":["input tex-base","[tex] tex-base"],"[tex] textcomp":["input textmacros":["input textmacros"],"[tex] to typeerror("invalid unicode":["input verb":["input>