var Comments = { url: "/comments/" };

Comments.Xhr = function(){
    /* plume Xhr version r1 */

    /**
     * Create XMLHttpRequest
     * @param method http-method name in uppercase. For example, GET, POST, etc.
     * @param url requested url. Possible with query-string. For example /post/1, /post?id=1
     * @param options options. Possible options are:
     *   onRequest - function to execute before request is made
     *   onSuccess - function to execute after receiving http 200 OK
     *   onFailure - function to execute after receiving status other than 200 OK
     *
     * Usage:
     *    new Xhr('GET', '/post?id=1', {
     *      onRequest: function(args) { alert("request: " + args); }
     *      onSucccess: function() { alert("success: " + this.responseText); }
     *      onFailure: function() { alert("faulure: " + this.status); }
     *    ).send();
     */
    var Xhr = function(method, url, options) {
        options = options || {};

        var factories = [
            function () { return new XMLHttpRequest(); },
            function () { return new ActiveXObject("Msxml2.XMLHTTP"); },
            function () { return new ActiveXObject("Microsoft.XMLHTTP"); }
        ];

        var xhr;
        for (var i = 0; i < factories.length; i++) {
            try { xhr = factories[i](); }
            catch (e) { continue; }
            break;
        }
        if (xhr == null)
            throw new Error("Current browser doesn't support XMLHttpRequest");

        this.method = method;
        this.url = url;
        this.xhr = xhr;

        this.onSuccess = options.onSuccess;
        this.onFailure = options.onFailure;
        this.onRequest = options.onRequest;

        this.requestHeaders = { 'User-Agent': 'XMLHTTP/1.0' };
        this.responseHeaders = {};

        this.status = null;
        this.statusText = null;
        this.readyState = null;

        if (method == 'POST')
            this.requestHeaders['Content-type'] = 'application/x-www-form-urlencoded';
    };

    /**
     * Invoked from native xhr.onreadystatechage
     */
    Xhr.prototype.onReadyStateChange = function() {
        this.readyState = this.xhr.readyState;
        if (this.readyState != 4) return;

        this.status = this.xhr.status;

        //in FF3 reading native xhr properties causes exception in case of network error
        var headers = "";
        try {
            this.statusText = this.xhr.statusText;
            headers = this.xhr.getAllResponseHeaders().split("\n");
        } catch (ignore) {}

        function trim(s) { return s.replace(/(^\s+)|(\s+$)/g, ""); }

        for (var i = 0; i < headers.length; i++) {
            var nameValue = headers[i].split(":");
            if (nameValue.length == 2)
                this.responseHeaders[trim(nameValue[0])] = trim(nameValue[1]);
        }

        if (this.status != 200) {
            if (this.onFailure) this.onFailure();
            return;
        }

        this.responseText = this.xhr.responseText;
        this.responseXml = this.xhr.responseXml;

        if (this.onSuccess) this.onSuccess();
    };

    /**
     * Sends request with specified args
     * @param args queryString or javascript object with arguments
     */
    Xhr.prototype.send = function(args) {
        /*
         Serializes javascript object to queryString.
         For example serialize({ a:1, b:[2, 3]}) will return "a=1&b=2&b=3"
         */
        function serialize(obj) {
            if (typeof(obj) == 'string') return obj.toString();

            var params = new Array();
            for (var name in obj) {
                var value = obj[name];

                if (typeof(value) == 'string' || typeof(value) == 'number' || typeof(value) == 'boolean')
                    params.push(encodeURIComponent(name) + "=" + encodeURIComponent(value));
                else if (value.constructor == Array) {
                    for (var i=0; i < value.length; i++)
                        params.push(encodeURIComponent(name) + "=" + encodeURIComponent(value[i]));
                }
            }

            var s = "";
            for (var j=0; j<params.length; j++) {
                if (s != "") s += "&";
                s += params[j];
            }

            return s;
        }

        var computedUrl = this.url;

        if (this.method=="GET") {
            computedUrl += computedUrl.indexOf("?") == -1 ? "?" : "&";
            computedUrl += Math.random();

            if (args) computedUrl += "&" + serialize(args);
        }

        if (this.onRequest) this.onRequest(args);
        this.xhr.open(this.method, computedUrl, true);

        var request = this;
        this.xhr.onreadystatechange = function() { request.onReadyStateChange(); };

        for (var name in this.requestHeaders)
            this.xhr.setRequestHeader(name, this.requestHeaders[name]);

        this.xhr.send(this.method == 'GET' || !args ? null : serialize(args));
    };

    /**
     * Returns string representation of object
     */
    Xhr.prototype.toString = function() {
        function join(o) {
            var s = "";
            for (n in o) s += (s != "" ? ", " : "") + "'" + n + "':'" + o[n] + "'";
            return s;
        }

        var s = "";
        s += "Xhr{ method:'" + this.method + "', url:'" + this.url + "',\n";
        s += "requestHeaders:{ " + join(this.requestHeaders) + " },\n";
        s += "responseHeaders:{ " + join(this.responseHeaders) + " },\n";
        s += "readyState:" + this.readyState + ", status:" + this.status + ", statusText:" + this.statusText + " }";
        return s;
    };

    return Xhr;
}();

/*
  сигнатура callback: function callback(obj),
  где obj - возвращенный json-объект, или null, если произошла ошибка http
*/
Comments.getTopic = function(topic, callback, from, max, order) {
    var xhr = new Comments.Xhr("GET", this.url + "topic/" + topic, {
        onSuccess: function() { callback(eval("(" + this.responseText + ")")); },
        onFailure: function() { callback(null); }
    });

    var args = {};
    if (from != null) args.from = from;
    if (max != null) args.max = max;
    if (order) args.order = order;

    xhr.send(args);
};

/*
  сигнатура callback: function callback(obj),
  где obj - возвращенный json-объект, или null, если произошла ошибка http
*/
Comments.postComment = function(topic, reply, text, callback) {
    var xhr = new Comments.Xhr("POST", this.url + "post", {
        onSuccess: function() { callback(eval("(" + this.responseText + ")")); },
        onFailure: function() { callback(null); }
    });

    var args = {
        topic: topic,
        text: text
    };
    if (reply) args.reply = reply;
    xhr.send(args);
};

Comments.deleteComment = function(comment, callback) {
    var xhr = new Comments.Xhr("GET", this.url + "delete", {
        onSuccess: function() { callback(eval("(" + this.responseText + ")")); },
        onFailure: function() { callback(null); }
    });

    xhr.send({comment: comment});
};

Comments.Panel = function(topic, options) {
    options = options || {};

    function CommentBlock(topic, comment) {
        var commentBlock = document.createElement("div");
        commentBlock.className = "comment-block";
        commentBlock.id = comment.id;

        //создаем head
        var head = document.createElement("div");
        head.className = "head";
        commentBlock.appendChild(head);

        //ссылка удалить
        if (comment.deletable) {
            var deleteLink = document.createElement("a");
            deleteLink.className = "delete-link";
            deleteLink.href = "";
            deleteLink.innerHTML = "удалить";
            head.appendChild(deleteLink);

            deleteLink.onclick = function() {
                if (confirm("Вы действительно хотите удалить комментарий?"))
                    Comments.deleteComment(comment.id, function(result) {
                        if (result == null) { panel.innerHTML = "<span style='color:red;'>Произошла ошибка соединения с сервером. Пожалуйста, повторите попытку позже.</span>"; return; }
                          panel.refresh(function() { panel.scrollToTop(); });
                    });

                return false;
            };
        }

        // ссылка на коммент
        var link = document.createElement("a");
        link.className = 'link';
        link.innerHTML = '#';
        link.href = '#' + comment.id;
        head.appendChild(link);        

        //автор
        var author = document.createElement("span");
        author.className="author";
        if (topic.currentUser == comment.author) author.className += " current-user";
        author.innerHTML = comment.author;
        head.appendChild(author);

        //дата создания     
        var created = document.createElement("span");
        created.className = "created";
        created.innerHTML = comment.created;
        head.appendChild(created);

        //cоздаем text
        function escapeHtml(s) {
            return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
                    .replace(/\n\r/g, "<br/>").replace(/\n/g, "<br/>").replace(/\r/g, "<br/>");
        }

        var text = document.createElement("div");
        text.className = "text";
        if (comment.text) text.innerHTML = escapeHtml(comment.text);
        commentBlock.appendChild(text);

        //ссылка ответить
        var replyLink = document.createElement("a");
        replyLink.className = "reply-link";
        replyLink.innerHTML = "ответить";
        replyLink.href="";
        commentBlock.appendChild(replyLink);        

        replyLink.onclick = function() {
            var form;
            for (var i=0; i<subComments.childNodes.length; i++) {
                var n = subComments.childNodes[i];
                if (n.nodeName == "FORM") { form = n; break; }
            }

            if (form) subComments.removeChild(form);
            else {
                var commentForm = new CommentForm(topic, comment);
                if (subComments.firstChild) subComments.insertBefore(commentForm, subComments.firstChild);
                else subComments.appendChild(commentForm);
                commentForm.focus(); //ставим фокус на форму
            }

            return false;
        };        

        //дочерние комментарии
        var subComments = document.createElement("div");
        subComments.className = "sub-comments";
        commentBlock.appendChild(subComments);
        if (comment.comments)
            for (var i=0; i<comment.comments.length; i++)
                subComments.appendChild(new CommentBlock(topic, comment.comments[i]));


        return commentBlock;
    }


    function CommentForm(topic, comment) {
        var form = document.createElement("form");
        form.className="comment-form";

        //кнопка закрыть есть, только когда пишем ответ
        if (comment) {
            var close = document.createElement("a");
            close.className="close-link";
            close.href="";
            close.innerHTML="&times;";
            close.onclick = function() {
                form.parentNode.removeChild(form);
                return false;
            };
            form.appendChild(close);
        }

        var title = document.createElement("div");
        title.className="title";
        title.innerHTML = comment ? "Добавить ответ" : "Добавить комментарий";
        form.appendChild(title);

        var errorsBlock = document.createElement("div");
        errorsBlock.className = "errors";
        errorsBlock.style['display'] = 'none';
        form.appendChild(errorsBlock);

        var text = document.createElement("textarea");
        form.appendChild(text);
        form.focus = function() { text.focus(); };

        text.onkeyup=function() { //лимит длины текста
            if (text.value.length > topic.maxCommentLength)
                text.value = text.value.substring(0, topic.maxCommentLength);
        };

        text.onkeydown=function(e) { //ctrl+Enter
            if (!e) e=window.event;

            if (e.keyCode == 13 && e.ctrlKey) {
                submit.click();
                return false;
            }
            
            return true;
        };

        //кнопки
        var buttons = document.createElement("div");
        buttons.className = "buttons";
        form.appendChild(buttons);

        //кнопка отправить
        var submit = document.createElement("button");
        submit.innerHTML = "Отправить";

        submit.onclick=function() {
            submit.disabled = true;

            Comments.postComment(topic.id, comment != null ? comment.id : null, text.value, function(response) {
                submit.disabled = false;
                if (response == null) { title.innerHTML = "<span style='color:red;'>Произошла ошибка соединения с сервером. Пожалуйста, повторите попытку позже.</span>"; return; }

                if (response.status=="error") {
                    errorsBlock.innerHTML = "";
                    for (var i=0; i<response.errors.length; i++) {
                        errorsBlock.appendChild(document.createTextNode(response.errors[i]));
                        errorsBlock.appendChild(document.createElement("br"));
                    }
                    errorsBlock.style['display'] = response.errors.length > 0 ? "block" : "none";

                    return;
                }

                //комментарий добавлен
                if (comment == null)
                    panel.page = panel.order == 'desc' ? 1 : panel.pagesCount;

                panel.refresh(function() { panel.scrollToTop(); });
            });

            return false;
        };
        buttons.appendChild(submit);
        buttons.appendChild(document.createTextNode(" "));

        return form;
    }


    function TopicPanel(topic) {
        var heading = document.createElement("div");
        heading.id = "comments-top";
        heading.className = "topic-panel";

        var total = document.createElement("div");
        total.className = "total";
        total.innerHTML = "Комментариев: " + topic.commentsInTopic;
        heading.appendChild(total);

        //порядок комментариев
        var orderLink = document.createElement("a");
        orderLink.href = "";
        orderLink.className = "order-link";
        orderLink.innerHTML = panel.order == "asc" ? "&darr;" : "&uarr;";
        orderLink.onclick = function() {
            panel.order = panel.order == 'asc' ? 'desc' : 'asc';
            panel.page = panel.order == 'desc' ? 1 : panel.pagesCount;
            panel.refresh(function() { panel.scrollToTop(); });
            return false;
        };
        heading.appendChild(orderLink);

        //кнопка обновить
        var refreshLink = document.createElement("a");
        refreshLink.className = "refresh-link";
        refreshLink.innerHTML = "обновить";
        refreshLink.href = "";
        refreshLink.onclick = function() { panel.refresh(function() { panel.scrollToTop(); }); return false; };
        heading.appendChild(refreshLink);

        return heading;
    }


    //посраничная навигация
    function PageNavigation(pagesCount, currentPage, callback) {
        var navigation = document.createElement("div");
        navigation.className = "page-navigation";

        for (var i=1; i<=pagesCount; i++) {
            var page = document.createElement("a");

            if (currentPage == i)
                page.className = "current";

            page.href="";
            page.innerHTML = "" + i;
            page.pageNumber = i;
            page.onclick = function() { callback(this.pageNumber); return false; };
            navigation.appendChild(page);
        }

        return navigation;
    }

    var panel = document.createElement('div');
    panel.className="comments";

    panel.page = 1;
    panel.pageSize = 10;
    panel.order = "desc";

    panel.scrollToTop = function() {
        var el = panel;
        var top = 0;
        do {
            top += el.offsetTop || 0;
            el = el.offsetParent;
        } while (el);

        window.scrollTo(0, top);
    };

    panel.refresh = function(callback) {
        for (var i = this.childNodes.length - 1; i >= 0; i--)
            this.removeChild(this.childNodes[i]);

        this.innerHTML = "<div class='loading'>Загрузка ...<div>";

        Comments.getTopic(topic, function(topic) {
            if (topic == null) { panel.innerHTML = "<span style='color:red;'>Произошла ошибка соединения с сервером. Пожалуйста, повторите попытку позже.</span>"; return; }

            panel.innerHTML = "";
            panel.pagesCount = Math.floor((topic.rootCommentsInTopic - 1) / panel.pageSize) + 1;

            //добавляем верхнюю панель
            panel.appendChild(new TopicPanel(topic));

            //добавляем комментарии в панель
            if (topic.comments)
                for (var i=0; i<topic.comments.length; i++)
                    panel.appendChild(new CommentBlock(topic, topic.comments[i]));

            //добавляем постраничку
            if (panel.pagesCount > 1)
                panel.appendChild(new PageNavigation(panel.pagesCount, panel.page, function(page) {
                    panel.page = page;
                    panel.refresh(function() { panel.scrollToTop(); });
                }));

            panel.appendChild(new CommentForm(topic, null));

            if (callback) callback(topic);
            if (options.onLoad) options.onLoad(topic);

        }, (panel.page - 1) * panel.pageSize, panel.pageSize, panel.order);
    };

    panel.refresh();
    return panel;
};

Comments.JsFrame = function() {
    /* plume JsFrame version r1 */

    /**
     * Create JsFrame using passed element as a container
     * @param el container for this jsframe
     */
    var JsFrame = function(el, options) {
        options = options || {};

        this.element = el;
        this.location = null;

        this.onLoad = options.onLoad;
        this.onRequest = options.onRequest;
        this.onFauilure = options.onFailure;

        //track link clicks inside element
        var frame = this;
        this.element.addEventListener("click", function(e) { frame.captureClicks(e); }, true);
        this.element.addEventListener("click", function(e) { frame.bubbleClicks(e); }, false);
    };

    /**
     * Returns absolute url based on current location and given url
     * @param url
     */
    JsFrame.prototype.getAbsoluteUrl = function(url) {
        if (url.indexOf("http://") == 0 || url.indexOf("https://") == 0 || url[0] == "/") return url;
        if (url == "") return this.location;

        var baseUrl = this.location;

        //удаляем query-string
        var questIdx = baseUrl.indexOf('?');
        if (questIdx != -1) baseUrl = baseUrl.substring(0, questIdx);

        if (url[0] == "?") return baseUrl + url;

        //удаляем компонент после /
        var slashIdx = baseUrl.lastIndexOf("/");
        if (slashIdx != -1) baseUrl = baseUrl.substring(0, slashIdx);

        return baseUrl + "/" + url;
    };

    /**
     * Sends request to specified url
     * @param method http method
     * @param url target url
     * @param data optional. Data to send
     */
    JsFrame.prototype.load = function(url, method, data) {
        method = method || "GET";

        var frame = this;
        var xhr = new Comments.Xhr(method, url, {
            onFailure: function() { if (frame.onFailure) frame.onFailure(url, method, data); },
            onSuccess: function() {
                var requestLocation = this.responseHeaders["Request-Location"];
                if (!requestLocation) requestLocation = url;
                frame.location = requestLocation;

                frame.element.innerHTML = this.responseText;
                frame.afterLoad();

                if (frame.onLoad) frame.onLoad(url, method, data);
            }
        });

        if (this.onRequest) this.onRequest(url, method, data);
        xhr.send(data);
    };

    /**
     * Executed after frame content is loaded. Method registers event listeners, etc.
     */
    JsFrame.prototype.afterLoad = function() {
        //evaluate scripts inside frame element
        var scripts = this.element.getElementsByTagName("script");
        for (var i=0; i<scripts.length; i++) {
            var script = scripts[i];
            eval(script.innerHTML);
        }

        //attach sumbmit listeners
        var forms = this.element.getElementsByTagName("form");
        for (i=0; i<forms.length; i++) {
            //handle input[@type=image] and input[@type=submit]
            var form = forms[i];
            var inputs = form.getElementsByTagName("input");

            var frame = this;
            for (var j=0; j<inputs.length; j++) {
                var input = inputs[j];
                if (input.type == 'submit' || input.type == 'image') {
                    function submitListener(e) {
                        e = e || window.event;

                        if (e.preventDefault) e.preventDefault();
                        e.returnValue = false;

                        frame.submitForm(form, this);
                    }

                    if (input.addEventListener) input.addEventListener("click", submitListener, false);
                    else if (input.attachEvent) input.attachEvent("click", submitListener);
                }
            }
        }
    };

    /**
     * Tracks link clicks inside frame element on capture phase
     * @param e event
     */
    JsFrame.prototype.captureClicks = function(e) {

        //track preventDefault invocations
        var preventDefault = e.preventDefault;
        e.preventDefault = function() {
            var t = this.preventDefault;
            this.preventDefault = preventDefault;
            this.preventDefault();
            this.preventDefault = t;

            this.defaultPrevented = true;
        };

        var target = e.target;
        if (target.onclick) {

            //track result returned from onclick
            var onclick = target.onclick;
            target.onclick = function(e) {
                var t = this.onclick;
                this.onclick = onclick;
                var clickResult = this.onclick(e);
                this.onclick = t;

                //note: clickResult may be undefined
                //noinspection PointlessBooleanExpressionJS
                e.defaultPrevented = clickResult == false;
                return clickResult;
            };
        }
    };

    /**
     * Tracks link clicks inside frame element on bubble phase
     * @param e event
     */
    JsFrame.prototype.bubbleClicks = function(e) {
        var target = e.target;

        if (target.nodeName != "A" || !target.href) return;
        if (target.href.indexOf("javascript") == 0) return;
        if (target.target == "_blank") return;
        if (e.defaultPrevented) return;

        //reload jsframe content
        e.preventDefault();
        var href = this.getAbsoluteUrl(target.getAttribute("href"));
        this.load(href, "GET");
    };

    /**
     * @param form
     * @param submiter
     */
    JsFrame.prototype.submitForm = function(form, submiter) {
        function serialize(form, submiter) {
            var qs = "";

            var addArg = function(name, value) {
                if (!name) return;
                if (qs != "") qs += "&";
                qs += encodeURIComponent(name) + "=";
                if (value) qs += encodeURIComponent(value);
            };

            function collect(el) {
                if (el.nodeName == "TEXTAREA") addArg(el.name, el.value);
                else if (el.nodeName == "SELECT") addArg(el.name, el.options[el.selectedIndex].value);
                else if (el.nodeName == "INPUT") {
                        switch (el.type) {
                            case 'text': case 'hidden': case 'password': addArg(el.name, el.value); break;
                            case 'checkbox': case 'radio': if (el.checked) addArg(el.name, el.value); break;
                            case 'submit': case 'image': if (el == submiter) addArg(el.name, el.value); break;
                        }
                    }

                for (var i=0; i<el.childNodes.length; i++)
                    collect(el.childNodes[i]);
            }
            collect(form);

            return qs;
        }

        var url = this.getAbsoluteUrl(form.action);
        var method = form.method ? form.method.toUpperCase() : "GET";

        if (method == "GET") { //если GET, то нужно убрать queryString из url
            var questIdx = url.indexOf("?");
            if (questIdx != -1) url = url.substr(0, questIdx);
        }

        this.load(url, method, serialize(form, submiter));
    };

    return JsFrame;
}();

Comments.Manager = function() {
    var el = document.createElement("div");
    var frame = new Comments.JsFrame(el);
    frame.load(Comments.url + "manage");
    return el;
};

