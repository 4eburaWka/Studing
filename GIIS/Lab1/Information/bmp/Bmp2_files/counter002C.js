(function(){var s=Math.random()<_atc.famp,A=_ate,y=document,n=window,g={},m={},u={},p={};function r(w,d,a){w/=d;w=Math.round(w*10)/10;if((w+"").length>4){w=Math.round(w);}return w+a;}function k(a){var d=(""+a).split(".").shift().length;if(isNaN(a)){return a;}else{if(d<4){return Math.round(a);}else{if(d<7){return r(a,1000,"K");}else{if(d<10){return r(a,1000000,"M");}else{return r(a,1000000000,"B");}}}}}function q(d){try{if(n.JSON&&n.JSON.parse){return JSON.parse(d);}}catch(a){return{};}}function o(d){try{if(n.JSON&&n.JSON.stringify){return JSON.stringify(d);}}catch(a){return"";}}function i(d){var a=_ate.cookie.rck("_atshc");if(a){return(q(a)||{})[d]||-1;}return-1;}function e(d,w){var a=_ate.cookie.rck("_atshc"),C;if(a){a=q(a);C=(a||{})[d]||0;if(C&&w>=C){delete a[d];_ate.cookie.sck("_atshc",o(a),1,1);}}}function z(d){var a=_ate.cookie.rck("_atshc"),w=B(d)+1;d.shares=w;v(d,k(w));if(!a){a={};}else{a=q(a);}if(a[d.url]){delete a[d.url];}m[d.url]=a[d.url]=w;_ate.cookie.sck("_atshc",o(a),1,1);}function B(a){var d=0;if(a&&a.shares){d=a.shares;if(isNaN(d)){d=0;}}return d;}function v(a,I){if(!a){return;}var M=a.className.indexOf("pill_style")>-1,J=(parseInt(I)!==0),E=!a.firstChild,K=a.addthis_conf||{},L=a.addthis_share||{};if(a.firstChild&&a.firstChild.nodeType==3){a.removeChild(a.firstChild);}if(E){var D=y.ce("a"),w=y.ce("a"),d=y.ce("span"),H=y.createTextNode("Share"),F=(document.compatMode=="BackCompat"),C=[],G;a.style.display="none";D.className="addthis_button_expanded";w.className="atc_s addthis_button_compact";w.appendChild(d);if(J&&M){a.className+=" addthis_nonzero";}if(F&&_ate.bro.msi&&M){D.style.lineHeight="20px";}K.ui_offset_top=(_ate.bro.msi?0:20)+(_ate.bro.ffx&&!F?15:0);K.ui_offset_left=0;K.product="sco"+(M?"pl":"")+"-"+_atc.ver;if(M){C=[w,D];}else{C=[D,w];}while(G=C.shift()){a.appendChild(G);}addthis.button(w,K,L);addthis._render([D],{conf:K,share:L},{nohover:true,singleservice:"more"});}I=y.createTextNode(I);if(!M){if(a.firstChild&&a.firstChild.firstChild){a.firstChild.removeChild(a.firstChild.firstChild);}(a.firstChild)?a.firstChild.appendChild(I):a.appendChild(I);}else{if(a.firstChild&&a.firstChild.nextSibling&&a.firstChild.nextSibling.firstChild){a.firstChild.nextSibling.removeChild(a.firstChild.nextSibling.firstChild);}if(!J){if(a.className){a.className=a.className.replace(/addthis_nonzero/g,"");}}else{if(a.className.indexOf("addthis_nonzero")==-1){a.className+=" addthis_nonzero";}a.firstChild.nextSibling.appendChild(I);}}a.style.display="block";a.href="#";}function c(a,d){a.shares=d;v(a,k(d));}function l(d,D,E,a){var w=0,C=i(d.url);if(D.error){w="?";}else{w=D.shares;}if(!isNaN(C)&&((isNaN(w)&&C>0)||C>w)){w=C;}else{e(d.url,w);}if(!m[d.url]){m[d.url]=w;}if(a){E(d,D);}else{E(d,w);}}function b(d,C){if(!d){C({error:{message:"no url provided",code:-10}});}if(p[d]){C(p[d]);}var a=d,w=_ate.util.scb("sc",d,function(E){if(s){var F=((new Date()).getTime()-_ate.cbs["time_"+w]),D=new Image();A.imgz.push(D);D.src="//m.addthisedge.com/live/t00/mu.gif?a=sc&r="+(1/s)+"&"+(isNaN(F)?"err=1":"t="+F);}if(!E.url){E.url=d;}p[d]=E;C(p[d]);},function(){p[d]={error:{message:"server timed out",code:999}};C(p[d]);});a=A.util.gUD(d).toLowerCase()+A.util.gUQS(d);_ate.ajs("//api-public.addthis.com/url/shares.json?url="+_euc(a)+"&callback="+w,1);}function x(d,D,a){var C=i(d.url),w=d.url;if(!u[w]){u[w]=[];}u[w].push(d);_ate.ed.addEventListener("addthis.menu.share",function(E){try{if(E.data.service&&_ate.track.mgu(E.data.url,{clean:1,defrag:1})==w){if(E.data.service=="facebook_unlike"||(_atc.ver>=300&&(E.data.service=="more"||E.data.service=="email"))||E.data.service=="google_unplusone"){return;}z(d);}}catch(E){}});if(m[w]!==undefined){D(d,m[w]);}else{if(w){if(!isNaN(C)&&C>0){D(d,C);}_ate.track.apc("sco"+(d.className.indexOf("pill_style")>-1?"pl":"")+"-"+_atc.ver);if(u[w].length>1){return;}b(w,function(F){if(F&&!F.error&&F.shares){m[w]=F.shares;}if(u[w]){for(var E=0;E<u[w].length;E++){l(u[w][E],F,D);}}});}}}function j(F,w,E){if(F){F=_ate.util.select(F);for(var C=0;C<F.length;C++){var a=F[C],D=((a.parentNode||{}).className||"").indexOf("addthis_toolbox")>-1?addthis.util.getAttributes(a.parentNode,w,E):((((a.parentNode||{}).parentNode||{}).className||"").indexOf("addthis_toolbox")>-1?addthis.util.getAttributes(a.parentNode.parentNode,w,E):null),d=addthis.util.getAttributes(a,D?D.conf:w,D?D.share:E,true);if(!a.ost){if(a.className.indexOf("addthis_counter")==-1){a.className+=" addthis_counter";}if(_ate.bro.ie6&&a.className.indexOf("compatmode")==-1){a.className+=((a.className.indexOf("bubble_style")>-1)?" bubble":" ")+"compatmode"+_ate.bro.mod;}if(_ate.bro.ie6&&a.className.indexOf("ie6")==-1){a.className+=" ie6";}else{if(_ate.bro.ie7&&a.className.indexOf("ie7")==-1){a.className+=" ie7";}}a.url=(E||d.share||n.addthis_share||{}).trackurl||_ate.track.mgu((E||{}).url||d.share.url||(n.addthis_share||{}).url,{clean:1,defrag:1});a.addthis_conf=d.conf;a.addthis_share=d.share;a.ost=1;x(a,function(G,H){c(G,H);});}}}}function t(w,a,d){j(w,a,d);}function h(F,d,E){if(F){F=_ate.util.select(F);for(var w=0;w<F.length;w++){var D=F[w],C=((D.parentNode||{}).className||"").indexOf("addthis_toolbox")>-1?addthis.util.getAttributes(D.parentNode,d,E):null,a=addthis.util.getAttributes(D,C?C.conf:d,C?C.share:E,true);if(!D.ost){D.url=(E||a.share||n.addthis_share||{}).trackurl||_ate.track.mgu((E||{}).url||a.share.url||(n.addthis_share||{}).url,{clean:1,defrag:1});D.addthis_conf=a.conf;D.addthis_share=a.share;D.ost=1;b(D.url,function(G){D.innerHTML=G.error?"?":G.shares;});}}}}function f(){addthis.count=h;addthis.counter=t;addthis.data.getShareCount=function(d,a){if(!a){a=addthis_share;}b(typeof(a)=="string"?a:a.trackurl||a.url,d);};addthis.count.ost=1;addthis.counter.ost=1;}if(_adr.isReady){f();return t;}else{addthis.addEventListener("addthis.ready",f);return addthis;}})();