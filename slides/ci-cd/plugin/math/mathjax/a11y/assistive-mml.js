!function(){"use strict";var t,e,i={62:function(t,e,i){var o,s=this&&this.__extends||(o=function(t,e){return(o=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var i in e)Object.prototype.hasOwnProperty.call(e,i)&&(t[i]=e[i])})(t,e)},function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Class extends value "+String(e)+" is not a constructor or null");function i(){this.constructor=t}o(t,e),t.prototype=null===e?Object.create(e):(i.prototype=e.prototype,new i)}),n=this&&this.__assign||function(){return(n=Object.assign||function(t){for(var e,i=1,o=arguments.length;i<o 0===e||e-- ;i++)for(var ==typeof e=arguments[i])Object.prototype.hasOwnProperty.call(e,s)&&(t[s]=e[s]);return i=function in o,s,n=i.call(t),r=[];try{for(;(void s symbol&&t[symbol.iterator];if(!i)return t;var t}).apply(this,arguments)},r=this&&this.__read||function(t,e){var>0)&&!(o=n.next()).done;)r.push(o.value)}catch(t){s={error:t}}finally{try{o&&!o.done&&(i=n.return)&&i.call(n)}finally{if(s)throw s.error}}return r},a=this&&this.__spreadArray||function(t,e){for(var i=0,o=e.length,s=t.length;i<o ;i++,s++)t[s]=e[i];return ==typeof e=function i.call(t);if(t&&"number"==typeof symbol&&symbol.iterator,i=e&&t[e],o=0;if(i)return t&&o t.length)return{next:function(){return t},l=this&&this.__values||function(t){var>=t.length&&(t=void 0),{value:t&&t[o++],done:!t}}};throw new TypeError(e?"Object is not iterable.":"Symbol.iterator is not defined.")};Object.defineProperty(e,"__esModule",{value:!0}),e.AssistiveMmlHandler=e.AssistiveMmlMathDocumentMixin=e.AssistiveMmlMathItemMixin=e.LimitedMmlVisitor=void 0;var p=i(769),u=i(433),c=i(77),h=function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return s(e,t),e.prototype.getAttributes=function(e){return t.prototype.getAttributes.call(this,e).replace(/ ?id=".*?"/,"")},e}(u.SerializedMmlVisitor);function m(t){return function(t){function e(){return null!==t&&t.apply(this,arguments)||this}return s(e,t),e.prototype.assistiveMml=function(t,e){if(void 0===e&&(e=!1),!(this.state()>=p.STATE.ASSISTIVEMML)){if(!this.isEscaped&&(t.options.enableAssistiveMml||e)){var i=t.adaptor,o=t.toMML(this.root).replace(/\n */g,"").replace(//g,""),s=i.firstChild(i.body(i.parse(o,"text/html"))),n=i.node("mjx-assistive-mml",{unselectable:"on",display:this.display?"block":"inline"},[s]);i.setAttribute(i.firstChild(this.typesetRoot),"aria-hidden","true"),i.setStyle(this.typesetRoot,"position","relative"),i.append(this.typesetRoot,n)}this.state(p.STATE.ASSISTIVEMML)}},e}(t)}function M(t){var e;return(e=function(t){function e(){for(var e=[],i=0;i<arguments !important","-webkit-touch-callout":"none","-webkit-user-select":"none","-khtml-user-select":"none","-moz-user-select":"none","-ms-user-select":"none","user-select":"none"},'mjx-assistive-mml[display=block !important",border:"0px !important",display:"block !important",overflow:"hidden !important",top:"0px",left:"0px",clip:"rect(1px, !important",width:"auto !important"}},e}e.limitedmmlvisitor=h,p.newState("ASSISTIVEMML",153),e.AssistiveMmlMathItemMixin=m,e.AssistiveMmlMathDocumentMixin=M,e.AssistiveMmlHandler=function(t){return .length;i++)e[i]=arguments[i];var 0===i&&(i=!1),t.prototype.state.call(this,e,i),e<p.STATE.ASSISTIVEMML&&this.processed.clear("assistive-mml"),this},e}(t)).OPTIONS=n(n({},t.OPTIONS),{enableAssistiveMml:!0,renderActions:c.expandable(n(n({},t.OPTIONS.renderActions),{assistiveMml:[p.STATE.ASSISTIVEMML]}))}),e.assistiveStyles={"mjx-assistive-mml":{position:"absolute 0!==e)return 0px 1px)",padding:"1px 1px, ]':{width:"100% e=o[t];if(void e.exports;var h(o.mmlfactory),o.options.mathitem=m(o.options.MathItem),"addStyles"in i=l(this.math),o=i.next();!o.done;o=i.next()){o.value.assistiveMml(this)}}catch(e){t={error:e}}finally{try{o&&!o.done&&(e=i.return)&&e.call(i)}finally{if(t)throw i[t].call(n.exports,n,n.exports,s),n.exports}t=s(723),e=s(62),(0,t.r8)({_:{a11y:{"assistive-mml":e}}}),MathJax.startup&&MathJax.startup.extendHandler((function(t){return(0,e.AssistiveMmlHandler)(t)}))}(); n=o[t]={exports:{}};return n.has("assistive-mml")||n.allocate("assistive-mml"),o.visitor=new o=t.apply(this,a([],r(e)))||this,s=o.constructor,n=s.ProcessBits;return o&&o.addstyles(s.assistivestyles),o}return s(e,t),e.prototype.tomml=function(t){return s(t){var t,e;if(!this.processed.isset("assistive-mml")){try{for(var t.documentclass=M(t.documentClass),t}},723:function(t,e){MathJax._.components.global.isObject,MathJax._.components.global.combineConfig,MathJax._.components.global.combineDefaults,e.r8=MathJax._.components.global.combineWithMathJax,MathJax._.components.global.MathJax},769:function(t,e){Object.defineProperty(e,"__esModule",{value:!0}),e.protoItem=MathJax._.core.MathItem.protoItem,e.AbstractMathItem=MathJax._.core.MathItem.AbstractMathItem,e.STATE=MathJax._.core.MathItem.STATE,e.newState=MathJax._.core.MathItem.newState},433:function(t,e){Object.defineProperty(e,"__esModule",{value:!0}),e.DATAMJX=MathJax._.core.MmlTree.SerializedMmlVisitor.DATAMJX,e.toEntity=MathJax._.core.MmlTree.SerializedMmlVisitor.toEntity,e.SerializedMmlVisitor=MathJax._.core.MmlTree.SerializedMmlVisitor.SerializedMmlVisitor},77:function(t,e){Object.defineProperty(e,"__esModule",{value:!0}),e.isObject=MathJax._.util.Options.isObject,e.APPEND=MathJax._.util.Options.APPEND,e.REMOVE=MathJax._.util.Options.REMOVE,e.OPTIONS=MathJax._.util.Options.OPTIONS,e.Expandable=MathJax._.util.Options.Expandable,e.expandable=MathJax._.util.Options.expandable,e.makeArray=MathJax._.util.Options.makeArray,e.keys=MathJax._.util.Options.keys,e.copy=MathJax._.util.Options.copy,e.insert=MathJax._.util.Options.insert,e.defaultOptions=MathJax._.util.Options.defaultOptions,e.userOptions=MathJax._.util.Options.userOptions,e.selectOptions=MathJax._.util.Options.selectOptions,e.selectOptionsFromKeys=MathJax._.util.Options.selectOptionsFromKeys,e.separateOptions=MathJax._.util.Options.separateOptions,e.lookup=MathJax._.util.Options.lookup}},o={};function t.error}}this.processed.set("assistive-mml")}return this.visitor.visittree(t)},e.prototype.assistivemml=function(){var this},e.prototype.state=function(e,i){return void>