"use strict";
window.globalConst = {}, window.ownKeys = function (e, n) {
    var o = Object.keys(e);
    if (Object.getOwnPropertySymbols) {
        var t = Object.getOwnPropertySymbols(e);
        n && (t = t.filter((function (n) {
            return Object.getOwnPropertyDescriptor(e, n).enumerable
        }))), o.push.apply(o, t)
    }
    return o
}, window._objectSpread = function (e) {
    for (var n = 1; n < arguments.length; n++) {
        var o = null != arguments[n] ? arguments[n] : {};
        n % 2 ? ownKeys(Object(o), !0).forEach((function (n) {
            _defineProperty(e, n, o[n])
        })) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(o)) : ownKeys(Object(o)).forEach((function (n) {
            Object.defineProperty(e, n, Object.getOwnPropertyDescriptor(o, n))
        }))
    }
    return e
}, window._defineProperty = function (e, n, o) {
    return n in e ? Object.defineProperty(e, n, {
        value: o,
        enumerable: !0,
        configurable: !0,
        writable: !0
    }) : e[n] = o, e
}, window._typeof = function (e) {
    return "function" === typeof Symbol && "symbol" === typeof Symbol.iterator ? window._typeof = function (e) {
        return typeof e
    } : window._typeof = function (e) {
        return e && "function" === typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
    }, window._typeof(e)
};
var App = "app.js",
    VERSION = 100;
window._wxReady = !1, $(document).ready((function () {
    $.ajaxSetup({
        cache: !1
    })
}));
var _debug = !1,
    allUrl = document.location.href;
_debug = !(allUrl.indexOf("szwego.com") || allUrl.indexOf("szwego.com") >= 0), $("#J_GoTop").click((function () {
    $("html, body").animate({
        scrollTop: 0
    }, "fast")
})), console.log("-------------------app js 2.8.10"), window.reloadHome = function () {
    window.sessionStorage.removeItem("albumHomeTabPos"), window.history.replaceState(null, null, location.href.split("#")[0]), window.history.go(0)
}, window.goHome = function () {
    window.location.replace("#/album_home")
}, window.goPersonalHome = function (e) {
    e && window.location.replace("#/shop_detail/" + e)
}, window.reLogin = function () {
    window.history.replaceState(null, null, location.href.split("#")[0] + "#/pc_login"), window.history.go(0)
};
var motify = window.motify = {
    show: function (e, n, o) {
        var t = 2e3,
            a = "";
        switch ("string" == typeof e && (a = e.split("#$&")[0]), !$("body").is(".motify") && $(".motify").length <= 0 && $("body").prepend("<div class='motify'><div class='motify-inner'></div></div>"), $(".motify").css("display", "block"), $(".motify-inner").text(a), _typeof(n)) {
            case "undefined":
                n = t;
                break;
            case "number":
                n <= 0 && (n = t);
                break;
            case "function":
                o = n, n = 1200;
                break;
            default:
                n = t;
                break
        }
        setTimeout((function () {
            $(".motify").css("display", "none"), "function" === typeof o && o()
        }), n)
    }
};
window.getBtnLoadingSrc = function () {
    return "data:image/gif;base64,R0lGODlhEAAQAMQRACYmJri4u5CQkKGhoVxcXLq6ugYGBm5ubisrKzY2Nri4uI2NjWpqalhYWJ+fnwAAAP///////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh/wtYTVAgRGF0YVhNUDw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo4NTZDOEExMEMyMjI2ODExODhDNjg0NzQyMTc1OEU5OCIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo4RTIzQzY2RUJCMDExMUUxOEM4RkFCQ0U5MUQxQjAzQSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo4RTIzQzY2REJCMDExMUUxOEM4RkFCQ0U5MUQxQjAzQSIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M1IE1hY2ludG9zaCI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjhCNkM4QTEwQzIyMjY4MTE4OEM2ODQ3NDIxNzU4RTk4IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjg1NkM4QTEwQzIyMjY4MTE4OEM2ODQ3NDIxNzU4RTk4Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Af/+/fz7+vn49/b19PPy8fDv7u3s6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2Mi4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1cW1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0sKyopKCcmJSQjIiEgHx4dHBsaGRgXFhUUExIREA8ODQwLCgkIBwYFBAMCAQAAIfkEBQcAEQAsAAAAABAAEAAABU9gJI4RBJGkopAm+Tyiuoqt+MKxSp/Rjcqlkw8V0Y1exGTSwWQSAVBo04mKQpXY0WJBajSSWy6DEfESUGHRWGTWbkdrduMcecPJI68yjgoBACH5BAUHABEALAAAAAAQABAAAAVPYCSOkaKQpOOQJglBorqKrfjCsUqf0Y3KpZMPFdGNXsRkcsFkEh9QaNOJikKV2BGDQQIAkltuoxHxIlBh0Vhk1m5HazbgHHnDySOvMo4KAQAh+QQFBwARACwAAAAAEAAQAAAFT2AkjpHjkOSykCapKKK6iq34wrFKn9GNyqWTDxXRjV7EZJLBZBIhUGjTiYpCldhRo0F6PJJbbiIR8RpQYdFYZNZuR2v24xx5w8kjrzKOCgEAIfkEBQcAEQAsAAAAABAAEAAABU5gJI7RspAkw5Am6Tiiuoqt+MKxSp/Rjcqlkw8V0Y1exGSywWQSFVBo04mKQpXYUSJBgkCSW+7jEfF+SWHRWGTWbkdrtlf0hpNH82QcFQIAIfkEBQcAEQAsAAAAABAAEAAABU9gJI4Rw5Bk05AmuSyiuoqt+MKxSp/Rjcqlkw8V0Y1exGQywWQSHVBo04mKQpXY0eNBUiiSWy4EEvEWUGHRWGTWbkdrtuIcecPJI68yjgoBACH5BAUHABEALAAAAAAQABAAAAVPYCSOUdOQZJKQJskworqKrfjCsUqf0Y3KpZMPFdGNXsRk8sFkEhdQaNOJikKV2BEEQnI4kluuQhHxDlBh0Vhk1m5Ha7bjHHnDySOvMo4KAQAh+QQFBwARACwAAAAAEAAQAAAFT2AkjlGSkOTzkCbZNKK6iq34wrFKn9GNyqWTDxXRjV7EZBLCZBIZUGjTiYpCldhRIEBaLJJbrsMR8QpQYdFYZNZuR2v24hx5w8kjrzKOCgEAIfkEBQcAEQAsAAAAABAAEAAABU9gJI7R85AkBJEmmSSiuoqt+MKxSp/Rjcqlkw8V0Y1exGRSwWQSG1Bo04mKQpXYkcNBYjCSW+5iEfEeUGHRWGTWbkdrNuMcecPJI68yjgoBADs="
}, window.getLoadingSrc = function () {
    return "data:image/gif;base64,R0lGODlh2gCVAPcAAP///7Ozs/v7+9bW1uHh4fLy8rq6uoGBgTQ0NAEBARsbG8TExJeXl/39/VRUVAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh+QQFBQAAACwAAAAA2gCVAAAI/wABCBxIsKDBgwgTKlzIsKHDhxAjSpxIsaLFixgzatzIsaPHjyBDihxJsqTJkyhTqlzJsqXLlzBjypxJs6bNmzhz6tzJs6fPn0CDCh1KtKjRo0iTKl3KtKnTp1CjSp1KtarVq1izat3KtavXr2DDih1LtqzZs2jTql3Ltq3bt3Djyp1Lt67du3jz6t3Lt6/fv4ADCx5MuLDhw4gTK17MuLHjx5AjS55MubLly5gza97MubPnzx8ZJGAA+qaCBAoKDiBQGmWAAwUTyCa4IECA1iYJKFDggKDsBAMJ2DaA2+RuBbcF/h5owPaA4iUP7EYwcDmAAcOhm0SwGzYA67YDsP/WTjLAcdbLsQdYQFD9ePIUAyBAQHqgg+4GhQdv7hx+RQbzIeBAcgsoUF9CtYXHnn8VORCggM8xFF4ABrzHYHwOBtiQehFeiBGACCTHUIceZkSAdyXuNOFwFqaI0AIMHCDjjBCtmJ2LCs2oI4oN2VghjgrBuCOPQNZEYpETHZkQh0hKxCRD/FHYYpMIERAlcQ0laNuCVL44IZZLimhleEp2eV14PwoknkHqcXldc1OaKVwAJCb4XHhq2hanmQ3NmRyeZ1LI50T8RQgoAIUOCpF6YB7qp6IP8ffeoQAkCKlDWxJE6XV7XloQAUc2B6anF1nZKamopqrqqqy26uqrsMY/KuustNZq66245qrrrrz26uuvwAYr7LDEFmvsscgmq+yyzDbr7LPQRivttNRWa+212Gar7bbcduvtt+CGe1JAACH5BAUFAAAALF0AOgAYABcAAAiZAAEIHEiwoIIABRMqHIhAAYKCBxgslEhQgUWCCBIkUIjgYcWLAhloVMCxo4GBFkkKVKDxgEIGHR2gBHlg5EIADjpSTAlggMYEFBd29MjTgUaPPQ8cOIkRKUGRCwYaUKp0gMABCBDeJBiAakQCWxcO8Ooy7MKpB6Kaval1rduwBAwEmEv3LQC5dOu+jZt3rt2/gAMLHnxT7dqAACH5BAUFAAAALF4AOgAdAA4AAAiZAAEIHEhwYAAEBRMqXAjAAQIHCQMwHDjAQEEEGAk6UKBgosADByQOxIhQYACOJSeCPDBgZEaBCDh6FGhgpcuUKGcKZADSIgCSAAhwVCByIIGFA2z+zHiAI8SBBxIkYEAggIGWA3mGVNhxpwKpCVgGGGvgaNADCyYuQAA2QckFY8em1dmWKEECBuL69Bg1LNKxWGc6CIxUJ8OAACH5BAUFAAAALGQAOgAZABEAAAiPAAEIHAhgwYEFBBMqXMjgAIOEDxcCIDAg4YGLCREgkBggAMKBFw8Q1CgRQMcABEBiFOhAY0SFAzoaUCkSAAONDkoCMNCxIoCQAjVu1EngpECgAEgmVKAgAMEFPRUGQOBzKlMFUn2WdHBVQU6dC7sOJegUrE2mZsEeSJm2rVuFCeLKVfCyrdy7Cd4CwJuAbkAAIfkEBQUAAAAsawA6ABIAGAAACIsABzAYAKCgwYMIAzBACMAAQYYAGEg8yODAAYgRJxYcYPEiRIkLC3Y0gBFkQQMdMWYM2fHhx4kBLIYsyAABAowLDhAw6MAmgpkQCfq8qbLgUAckixr9qbSp06cFFUidSlTl1KsKimJVgCAAVKcHXDY9kCCBx6ZlyyoAihNB2gRVizJQkPasUrIJvAYEACH5BAUFAAAALGsAOgASAB4AAAipAAkYIACgoMGDCA0EMIBwAcKDASJCZMDgYcGIAQ5SzGgRo8EAFB12lAhgAcWKFgF4BHAy5UWJJhlwLGjgwIEBFgfMHGDTJkOXBBj0PIDS5dCbLg0u8JkU4cymUJMimErVwdOHVLMikKrVQdSvBgl+ZaBAAdiyZRFczekArQKvFg8kEBkAAVqLDhIk2HrQrkUCehMUbSo3gdmvCvQe+BogMFgEesVGJWoxIAAh+QQFBQAAACxsADsAEQAfAAAIpAABCBwIYAABgggRLggQIKFDAgwNOExogOGAiQQHRMRIkGGAgxwLMlyQkSFIgicBEKhokeNCjyQxegxgIKVDjQEuhhSoc6dPhweCCmUQE6jQoxiPBiX6s6nPAAgQMPAZNaqDn1URTGSggKCDqlMJHlCg4OrAqVoBJFgrkKyChg7XJhhINm1CuQMRkJ2Il+7eu2wHOviLsG9HhwoSdPXJIEHYnQEBACH5BAUFAAAALGUASAAYABIAAAiTAAEIHEiwIIAACBMaIGCw4cCEEA04dAgR4cKJGDNiDKAR44IDByR2NAiy5ICRBAkwKHmAwcgACE4CGMBSJIAFCQ40RICgoAGQMgEgSJDAAQAFSAXy7DmRAdEEDJEqEMiAp1GHCojqPJpUoAOeLkkSnSpQKsGlDbMmCMuV7ECeDYkyLdt1INuCKwsiUDAX5UO3GgMCACH5BAUFAAAALF8ATAAdAA4AAAigAAEIHEiwoEEAAw4SHOBAocEBAQIkPHggQYIDDgkaiBjAAAGCARRYtJiR4AKOARYIRDAyAQKVDhcc+AiAwMaIAypaVMBA4ACeBgMcONBz4ICNBBhYxDjQgQIFGBFIFTj0wESDNAeGfLpyKgADVUsORMC1K4KBDIYaEAvg6VmzRsOWJKsgwFivAtMyzfi04d23Aw1cdWi3oAMEftmKBVwyIAAh+QQFBQAAACxdAEkAGQARAAAIjQAZKEhAsCCAgwgTKjxYsGGChRATCnT4MKLFixgvEjiQEaMCBQw6QkTw8aPIhA5KKnCAcUCAhSURvDwoc6HLAAsSBjCpEAGCgweCHgxAlABGnz8BBOUI4KaBiw58hlQq9KABogMiMvDJEmhVAASIzhyZ1CvTgwuIRvSpcKnCAUa1KmRwYOpJhQsO5FwYEAAh+QQFBQAAACxeAEIAEQAYAAAIgQADJEhwAIDBgwgPHhiYQAGDhBABIGCYAMGCiAgZKKCIMeFCgh0TDigYsqTJkyhTqlyJkQECBCYNOHj5siRNmAM6unzp4CCBAxchvnx4kMGBAwEABFiKceRRg0uTRjx6wABUphANUD0YderRnFelekSKsCvEAWINGghg9SQBAwQCAgAh+QQFBQAAACxdADwADgAdAAAImQABCBwIgMEBgggHJkiAICHChQkCOBx4YKGCiQMVLDyIkQHEARkbEkSw0EFGBQoQSASwIAFHgQ5QonQA0mEABDIvYgSAksFOAAR+7gzgAIHRowmPKhVJkOhSpkKjrsRo4MCBBRMHWN3q0OBWBkERVrXKAKvAAGEBaD1ggOCCAAFqOiQAd6pDA3DlJhwAty1VuGltBjCLkYDegAA7"
}, window.getLoadingImg = function (e) {
    var n = e || "正在加载...";
    return '<div class="loadingImg"><img src="'.concat(getLoadingSrc(), '" width="109" height="75"><span class="loading-txt" style="color:#999;">').concat(n, "</span></div>")
};
var loading = window.loading = {
        is_loading: !1,
        text_bak: "",
        btn_obj: null,
        is_btn: !1,
        show: function (e, n) {
            this.is_loading || (this.text_bak = e.text(), this.btn_obj = e, this.is_loading = !0, n && n.length > 0 && this.btn_obj.text(n), "button" == e.get(0).tagName.toLowerCase() ? e.attr("disabled", "true") : e.css({
                "pointer-events": "none"
            }), this.is_btn = !0, e.prepend('<img src="'.concat(getBtnLoadingSrc(), '" width="10" height="10">&nbsp;')))
        },
        remove: function () {
            this.is_loading = !1, this.btn_obj && this.btn_obj.text(this.text_bak), this.is_btn && (this.is_btn = !1, this.btn_obj.removeAttr("disabled").css({
                "pointer-events": "auto"
            }))
        }
    },
    loadingImg = window.loadingImg = {
        is_loading: !1,
        show: function (e, n) {
            this.is_loading || (this.is_loading = !0, n ? e.after(getLoadingImg(n)) : e.after(getLoadingImg()))
        },
        remove: function () {
            $(".loadingImg").remove(), this.is_loading = !1
        }
    };
$(".js-anchor-back").click((function (e) {
    return $(this).parent().parent().hide(), window.history.replaceState(null, null, location.href.split("#")[0]), !1
})), $(".js-open-anchor").click((function (e) {}));
var addEvent = window.addEvent = function (e, n) {
    document.getElementById(e).addEventListener("click", (function (e) {
        if (!window.WeixinJSBridge) return alert("请确认您是在微信内置浏览器中打开的"), e.preventDefault(), !1;
        n(this, e)
    }), !1)
};
window.changeShareURL = function (e) {
    var n = e,
        o = new Array;
    return o = e.split("."), n = e.replace(o[0], "https://www"), n
}, window._shareFriend = function (e, n, o) {
    wx.onMenuShareAppMessage({
        title: e.title,
        desc: e.desc,
        link: changeShareURL(e.link),
        imgUrl: e.cover,
        type: "",
        dataUrl: "",
        success: function () {
            n && n()
        },
        cancel: function () {
            o && o(), console.log("theData:\n".concat(e)), console.log("wx:\n".concat(this.title, "\n").concat(this.desc, "\n").concat(this.link, "\n").concat(this.imgUrl))
        }
    })
}, window._shareTimeline = function (e, n, o) {
    wx.onMenuShareTimeline({
        title: e.title,
        desc: e.desc,
        link: changeShareURL(e.link),
        imgUrl: e.cover,
        type: "",
        dataUrl: "",
        success: function () {
            n && n()
        },
        cancel: function () {
            o && o(), console.log("theData:\n".concat(e)), console.log("wx:\n".concat(this.title, "\n").concat(this.desc, "\n").concat(this.link, "\n").concat(this.imgUrl))
        }
    })
}, window._shareQZone = function (e, n, o) {
    wx.onMenuShareQZone({
        title: e.title,
        desc: e.desc,
        link: e.link,
        imgUrl: e.cover,
        success: function () {
            n && n()
        },
        cancel: function () {
            o && o(), console.log("theData:\n".concat(e)), console.log("wx:\n".concat(this.title, "\n").concat(this.desc, "\n").concat(this.link, "\n").concat(this.imgUrl))
        }
    })
}, window._shareQQ = function (e, n, o) {
    wx.onMenuShareQQ({
        title: e.title,
        desc: e.desc,
        link: e.link,
        imgUrl: e.cover,
        success: function () {
            n && n()
        },
        cancel: function () {
            o && o(), console.log("theData:\n".concat(e)), console.log("wx:\n".concat(this.title, "\n").concat(this.desc, "\n").concat(this.link, "\n").concat(this.imgUrl))
        }
    })
}, window._shareWeibo = function (e, n, o) {
    wx.onMenuShareWeibo({
        title: e.title,
        desc: e.desc,
        link: e.link,
        imgUrl: e.cover,
        success: function () {
            n && n()
        },
        cancel: function () {
            o && o(), console.log("theData:\n".concat(e)), console.log("wx:\n".concat(this.title, "\n").concat(this.desc, "\n").concat(this.link, "\n").concat(this.imgUrl))
        }
    })
}, window.chooseOwnImage = function (e, n, o) {
    var t = 9;
    n && (t = n > 9 ? 9 : n), wx.chooseImage({
        count: t,
        success: function (n) {
            var o = n.localIds;
            console.log(o), console.log(o.length), e && e(o)
        },
        fail: function (n) {
            alert("choose:".concat(JSON.stringify(n))), e && e(null)
        },
        cancel: function () {
            console.log("用户点击了取消", o), o && o()
        }
    })
}, window.uploadOwnImage = function (e, n, o) {
    wx.uploadImage({
        localId: e.toString(),
        isShowProgressTips: n,
        success: function (e) {
            var n = e.serverId;
            console.log(n), o && o(n)
        },
        fail: function (e) {
            alert("upload:".concat(JSON.stringify(e))), o && o(null)
        }
    })
}, window.previewOwnImage = function (e, n) {
    wx.previewImage({
        current: e,
        urls: n
    })
}, window._getNetworkType = function (e) {
    wx.getNetworkType({
        success: function (n) {
            var o = n.networkType;
            e && e(o)
        },
        fail: function (n) {
            alert(JSON.stringify(n)), e && e(null)
        }
    })
}, window._openLocation = function (e) {
    wx.openLocation({
        latitude: e.latitude,
        longitude: e.longitude,
        name: e.name,
        address: e.address,
        scale: e.scale,
        infoUrl: e.infoUrl
    })
}, window.openAddr = function (e) {
    wx.openAddress({
        trigger: function (n) {
            e(n, "trigger")
        },
        success: function (n) {
            e(n, "success")
        },
        cancel: function (n) {
            e(n, "cancel")
        },
        fail: function (n) {
            e(n, "fail")
        }
    })
}, window._getLocation = function (e, n) {
    wx.getLocation({
        type: e,
        success: function (e) {
            var o = e.latitude,
                t = e.longitude,
                a = e.speed,
                i = e.accuracy;
            n && n(o, t, a, i)
        },
        fail: function (e) {
            alert(JSON.stringify(e)), n && n(null)
        }
    })
}, window._hideMenuItems = function (e, n, o) {
    wx.hideMenuItems({
        menuList: e,
        success: function (e) {
            n && n()
        },
        fail: function (e) {
            o && o()
        }
    })
}, window._scanQRCode = function (e, n, o) {
    var t = {
        needResult: 1,
        scanType: ["qrCode", "barCode"],
        success: function (n) {
            var o = n.resultStr;
            console.log(o), e && e(o)
        },
        fail: function (e) {
            console.log(e), loading.remove(), o ? o(e) : motify.show("扫描失败，请稍后重试~")
        },
        cancel: function (e) {
            console.log(e), loading.remove(), n && n(e)
        }
    };
    e ? wx.scanQRCode(t) : wx.scanQRCode()
}, window.wxConfig = function (e) {
    wx.config({
        debug: e.debug,
        appId: e.appId,
        timestamp: e.timestamp,
        nonceStr: e.nonceStr,
        signature: e.signature,
        jsApiList: e.jsApiList,
        openTagList: ["wx-open-launch-app", "wx-open-launch-weapp"]
    })
}, window.wxPay = function (e, n, o, t) {
    function a() {
        WeixinJSBridge.invoke("getBrandWCPayRequest", {
            appId: e.appId,
            timeStamp: e.timeStamp,
            nonceStr: e.nonceStr,
            package: e.packages,
            signType: e.signType,
            paySign: e.paySign
        }, (function (e) {
            switch (console.log("pay res: ".concat(JSON.stringify(e))), loading.remove(), e.err_msg) {
                case "get_brand_wcpay_request:ok":
                    n && n();
                    break;
                case "get_brand_wcpay_request:cancel":
                    o && o();
                    break;
                case "get_brand_wcpay_request:fail":
                    t ? t(e.err_desc) : motify.show("支付失败，请稍后重试~");
                    break;
                default:
                    motify.show("支付失败，请稍后重试~");
                    break
            }
        }))
    }
    "undefined" === typeof WeixinJSBridge ? document.addEventListener ? document.addEventListener("WeixinJSBridgeReady", a, !1) : document.attachEvent && (document.attachEvent("WeixinJSBridgeReady", a), document.attachEvent("onWeixinJSBridgeReady", a)) : a()
}, window.initWxJs = function (e, n, o) {
    n.indexOf("#") >= 0 && (n = n.substring(0, n.indexOf("#")));
    var t = encodeURIComponent(n);
    if (1 != window._wxReady) {
        var a = getAjaxUrl("/service/jsapi_service.jsp?act=get_config&shop_id=".concat(e, "&url=").concat(t)),
            i = getAppendHeader();
        $.ajax({
            type: "get",
            url: a,
            headers: i,
            success: function (e, n, t) {
                console.log("wxConfig:", e);
                try {
                    "function" === typeof window._xhrSuccessHook && window._xhrSuccessHook({
                        url: a,
                        type: "get",
                        headers: i,
                        data: e,
                        resHeaders: t.getAllResponseHeaders(),
                        jqXHR: t
                    })
                } catch (A) {
                    console.error(A)
                }
                0 == e.errcode && (wxConfig(e.config), window._wxReady = !0, window._wxReady && wx.ready((function () {
                    o && ("share" == o.type ? (_shareFriend(o.data, o.successDo, o.cancelDo), _shareTimeline(o.data, o.successDo, o.cancelDo), _shareQZone(o.data, o.successDo, o.cancelDo), _shareQQ(o.data, o.successDo, o.cancelDo), _shareWeibo(o.data, o.successDo, o.cancelDo)) : "chooseImage" == o.type ? chooseOwnImage(o.callback, o.count, o.fail) : "uploadImage" == o.type ? uploadOwnImage(o.localId, o.isShowProgressTips, o.callback) : "previewImage" == o.type ? previewOwnImage(o.current, o.urls) : "getNetworkType" == o.type ? _getNetworkType(o.callback) : "openLocation" == o.type ? _openLocation(o.data) : "getLocation" == o.type ? _getLocation(o.typeOwn, o.callback) : "hideMenuItems" == o.type ? _hideMenuItems(o.menuList, o.success, o.fail) : "openAddress" == o.type ? openAddr(o.callback) : "shareFriend" == o.type ? _shareFriend(o.data, o.successDo, o.cancelDo) : "shareTimeline" == o.type ? _shareTimeline(o.data, o.successDo, o.cancelDo) : "shareQZone" == o.type ? _shareQZone(o.data, o.successDo, o.cancelDo) : "shareQQ" == o.type ? _shareQQ(o.data, o.successDo, o.cancelDo) : "shareWeibo" == o.type ? _shareWeibo(o.data, o.successDo, o.cancelDo) : "hideOption" == o.type ? wxJsBridgeReady(_wx.hide_option) : "showOption" == o.type ? wxJsBridgeReady(_wx.show_option) : "scanQRCode" == o.type ? _scanQRCode(o.successDo, o.cancelDo, o.failDo) : alert("type参数错误~"))
                })))
            },
            error: function (e) {
                0
            }
        })
    }
    console.log(o)
}, window.wxJsBridgeReady = function (e) {
    e && "function" === typeof e && ("undefined" === typeof window.WeixinJSBridge ? document.addEventListener ? document.addEventListener("WeixinJSBridgeReady", e, !1) : document.attachEvent && (document.attachEvent("WeixinJSBridgeReady", e), document.attachEvent("onWeixinJSBridgeReady", e)) : e())
}, window.wx_init = function (e) {
    window._wxReady || (_debug || e ? initWxJs("", window.location.href, {
        type: "showOption"
    }) : initWxJs("", window.location.href, {
        type: "hideOption"
    }))
};
var _wx = window._wx = {
        share: function (e, n, o) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "share",
                data: e,
                successDo: n,
                cancelDo: o
            }), console.log(window._wxReady), window._wxReady && wx.ready((function () {
                _shareFriend(e, n, o), _shareTimeline(e, n, o)
            })), console.log(e)
        },
        shareFriend: function (e, n, o) {
            var t = ["menuItem:share:timeline"];
            _wx.hideMenuItems(t), window._wxReady || initWxJs("", window.location.href, {
                type: "shareFriend",
                data: e,
                successDo: n,
                cancelDo: o
            }), console.log(window._wxReady), window._wxReady && wx.ready((function () {
                _shareFriend(e, n, o)
            })), console.log(e)
        },
        shareTimeline: function (e, n, o) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "shareTimeline",
                data: e,
                successDo: n,
                cancelDo: o
            }), console.log(window._wxReady), window._wxReady && wx.ready((function () {
                _shareTimeline(e, n, o)
            })), console.log(e)
        },
        shareQZone: function (e, n, o) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "shareQZone",
                data: e,
                successDo: n,
                cancelDo: o
            }), console.log(window._wxReady), window._wxReady && wx.ready((function () {
                _shareQZone(e, n, o)
            })), console.log(e)
        },
        shareQQ: function (e, n, o) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "shareQQ",
                data: e,
                successDo: n,
                cancelDo: o
            }), console.log(window._wxReady), window._wxReady && wx.ready((function () {
                _shareQQ(e, n, o)
            })), console.log(e)
        },
        shareWeibo: function (e, n, o) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "shareWeibo",
                data: e,
                successDo: n,
                cancelDo: o
            }), console.log(window._wxReady), window._wxReady && wx.ready((function () {
                _shareWeibo(e, n, o)
            })), console.log(e)
        },
        chooseImage: function (e, n, o) {
            var t = 9;
            n && (t = n, t > 9 && (t = 9)), window._wxReady || (console.log("----!wxReady"), initWxJs("", window.location.href, {
                type: "chooseImage",
                count: t,
                callback: e,
                fail: o
            })), window._wxReady && (console.log("----wxReady"), wx.ready((function () {
                chooseOwnImage(e, n, o)
            })))
        },
        uploadImage: function (e, n, o) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "uploadImage",
                localId: e,
                isShowProgressTips: n,
                callback: o
            }), window._wxReady && wx.ready((function () {
                uploadOwnImage(e, n, o)
            }))
        },
        previewImage: function (e, n) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "previewImage",
                current: e,
                urls: n
            }), window._wxReady && wx.ready((function () {
                previewOwnImage(e, n)
            }))
        },
        getNetworkType: function (e) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "getNetworkType",
                callback: e
            }), window._wxReady && wx.ready((function () {
                _getNetworkType(e)
            }))
        },
        openLocation: function (e) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "openLocation",
                data: e
            }), window._wxReady && wx.ready((function () {
                _openLocation(e)
            }))
        },
        openAddress: function (e) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "openAddress",
                callback: e
            }), window._wxReady && wx.ready((function () {
                openAddr(e)
            }))
        },
        getLocation: function (e, n) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "getLocation",
                typeOwn: e,
                callback: n
            }), window._wxReady && wx.ready((function () {
                _getLocation(e, n)
            }))
        },
        hideMenuItems: function (e, n, o) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "hideMenuItems",
                menuList: e,
                success: n,
                fail: o
            }), window._wxReady && wx.ready((function () {
                _hideMenuItems(e, n, o)
            }))
        },
        scanQRCode: function (e, n, o) {
            window._wxReady || initWxJs("", window.location.href, {
                type: "scanQRCode",
                successDo: e,
                cancelDo: n,
                failDo: o
            }), window._wxReady && wx.ready((function () {
                _scanQRCode(e, n, o)
            }))
        },
        hide_option: function () {
            WeixinJSBridge.call("hideOptionMenu")
        },
        show_option: function () {
            WeixinJSBridge.call("showOptionMenu")
        },
        hideMenu: function () {
            wxJsBridgeReady(_wx.hide_option)
        },
        showMenu: function () {
            wxJsBridgeReady(_wx.show_option)
        },
        isMiniapp: function () {
            if (window.location.search.indexOf("is_miniapp_env=1") > -1) return !0;
            var e = sessionStorage.getItem("is_miniapp_env");
            return "1" === e || navigator.userAgent.indexOf("miniProgram") > -1
        },
        is_wx: function () {
            return /MicroMessenger/i.test(navigator.userAgent) && !_wx.isMiniapp()
        },
        pay: function (e, n, o, t) {
            var a = e.tradeType;
            if ("APP" == a) g_wxpayCallback = n, g_cancelDo = o, appShare(6, e);
            else if ("JSAPI" == a) {
                if (!this.is_wx()) return loading.remove(), motify.show("请在微信中支付~"), !1;
                wxPay(e, n, o, t)
            } else "ALI_APP" == a ? (g_wxpayCallback = n, appShare(isMobile.iOS() ? 301 : 13, e)) : "ALIPAY_APP" == a ? (g_wxpayCallback = n, appShare(301, e)) : "APPLE" == a | "APPLE_APP" === a && (g_wxpayCallback = n, appShare(42, e))
        }
    },
    g_wxpayCallback, g_cancelDo;
window.appJavaPayResultCB = function (e) {
    "1" == e ? g_wxpayCallback && g_wxpayCallback(e) : (g_cancelDo && g_cancelDo(), loading.remove())
};
var isMobile = window.isMobile = {
        Android: function () {
            return !!navigator.userAgent.match(/Android/i)
        },
        BlackBerry: function () {
            return !!navigator.userAgent.match(/BlackBerry/i)
        },
        iOS: function () {
            return !!navigator.userAgent.match(/iPhone|iPad|iPod|iOS/i) || isMobile.iPad()
        },
        iPad: function () {
            var e = "MacIntel" === navigator.platform && navigator.maxTouchPoints > 1;
            return !!navigator.userAgent.match(/iPad/i) || e
        },
        Windows: function () {
            return !!navigator.userAgent.match(/IEMobile/i)
        },
        any: function () {
            return isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Windows()
        },
        AppAndroid: function () {
            return "android" == getPar("client_type") || "android" == ReactFn.getLocalData("client_type") || !!window["native"] && !!window["native"].appclienShare
        },
        AppIOS: function () {
            return "ios" == getPar("client_type") || "ios" == ReactFn.getLocalData("client_type") || !!window.webkit && !!window.webkit.messageHandlers && !!window.webkit.messageHandlers.webViewApp
        },
        AppClient: function () {
            return isMobile.AppAndroid() || isMobile.AppIOS()
        },
        Electron: function () {
            return !!navigator.userAgent.match(/Electron/i)
        },
        WegoAlbumPC: function () {
            return !!navigator.userAgent.match(/WegoAlbum/i)
        },
        isAppInput: function () {
            return isMobile.AppClient() && "1" == getPar("isKeyboardEnv")
        }
    },
    browser = window.browser = {
        isOpera: function () {
            return navigator.userAgent.indexOf("Opera") > -1
        },
        isFirefox: function () {
            return navigator.userAgent.indexOf("Firefox") > -1
        },
        isChrome: function () {
            return navigator.userAgent.indexOf("Chrome") > -1
        },
        isSafari: function () {
            return navigator.userAgent.indexOf("Safari") > -1
        },
        isIE: function () {
            return navigator.userAgent.indexOf("compatible") > -1 && navigator.userAgent.indexOf("MSIE") > -1 && !isOpera
        }
    };
window.getiOSversion = function () {
    var e = navigator.userAgent.match(/OS (\d+)_(\d+)_?(\d+)?/);
    return !!e && parseInt(e[1])
}, _debug ? wxJsBridgeReady(_wx.show_option) : wxJsBridgeReady(_wx.hide_option), window.is_weixin = function () {
    var e = navigator.userAgent.toLowerCase();
    return "micromessenger" == e.match(/MicroMessenger/i)
}, window.weixinPlat = function () {
    return is_weixin() || 1 == getPar("wg_debug")
}, window.mobilePlat = function () {
    return isMobile.any() || 1 == getPar("wg_debug")
}, window.setUrlParam = function (e, n, o) {
    var t = new RegExp("(\\?|&)".concat(n, "=([^&]+)(&|$)"), "i"),
        a = e.match(t);
    return a ? e.replace(t, (function (e, n, t) {
        return e.replace(t, o)
    })) : -1 == e.indexOf("?") ? "".concat(e, "?").concat(n, "=").concat(o) : "".concat(e, "&").concat(n, "=").concat(o)
}, window.getPar = function (e) {
    var n = new RegExp("(^|&)".concat(e, "=([^&]*)(&|$)"), "i"),
        o = window.location.search.substr(1).match(n);
    return null != o ? decodeURI(o[2]) : ""
}, window.getHeight = function (e, n, o) {
    var t;
    return e > o ? (o, t = o * n / e) : e == o ? (o, t = n) : (e, t = n), t
}, window.getPageScrollTop = function (e) {
    var n = document.documentElement && document.documentElement.scrollTop || document.body.scrollTop || 0;
    if (n) return n;
    if (e) {
        var o = document.body.style.top;
        return n = o ? Math.abs(parseInt(o)) : 0, n
    }
    return n
}, window.setPageScrollTop = function (e) {
    document.documentElement && (document.documentElement.scrollTop = e), document.body.scrollTop = e
};
var countDown = window.countDown = {
    timer: function (e, n, o) {
        var t = window.setInterval((function () {
            0 == e && (clearInterval(t), o && o());
            var a = 0,
                i = 0,
                A = 0,
                c = 0;
            e > 0 && (a = Math.floor(e / 86400), i = Math.floor(e / 3600) - 24 * a, A = Math.floor(e / 60) - 24 * a * 60 - 60 * i, c = Math.floor(e) - 24 * a * 60 * 60 - 60 * i * 60 - 60 * A), A <= 9 && (A = "0".concat(A)), c <= 9 && (c = "0".concat(c)), i <= 9 && (i = "0".concat(i)), a <= 9 && (a = "0".concat(a)), n ? n(a, i, A, c) : ($("#day_show").html(a), $("#hour_show").html('<s id="h"></s>'.concat(i)), $("#minute_show").html("<s></s>".concat(A)), $("#second_show").html("<s></s>".concat(c))), e--
        }), 1e3);
        return t
    },
    timerHour: function (e, n, o) {
        var t = window.setInterval((function () {
            0 == e && (clearInterval(t), o && o());
            var a = 0,
                i = 0,
                A = 0;
            e > 0 && (a = Math.floor(e / 3600), i = Math.floor(e / 60) - 60 * a, A = Math.floor(e) - 60 * a * 60 - 60 * i), i <= 9 && (i = "0".concat(i)), A <= 9 && (A = "0".concat(A)), a <= 9 && (a = "0".concat(a)), n ? n(a, i, A) : ($("#hour_show").html('<s id="h"></s>'.concat(a)), $("#minute_show").html("<s></s>".concat(i)), $("#second_show").html("<s></s>".concat(A))), e--
        }), 1e3);
        return t
    }
};
(function (e) {
    e.fn.longClick = function (n, o) {
        var t;
        o = o || 500, e(this).mousedown((function () {
            return t = setTimeout((function () {
                n()
            }), o), !1
        })), e(document).mouseup((function () {
            return clearTimeout(t), !1
        }))
    }
})(jQuery);
var changeTwoDecimal = window.changeTwoDecimal = function (e) {
    var n = parseFloat(e);
    if (isNaN(n)) return alert("function:changeTwoDecimal->parameter error"), !1;
    n = Math.round(100 * e) / 100;
    return n
};
window.LOG = function (e) {
    _debug && (console.log(e), alert(JSON.stringify(e)))
};
var RE_INT_GT0 = /^[1-9]+[0-9]*]*$/,
    RE_INT_GTE0 = /^[0-9]+[0-9]*]*$/,
    RE_FLOAT_GTE0 = /^[0-9]\d*(\.\d+)?$/;
window.IsNum = function (e, n, o) {
    if (null == e) return !1;
    var t = e.trim();
    return n && "" == t && (t = 0), o.test(t)
}, window._fileUploadInit = function (e, n, o, t, a, i, A, c) {
    var r = Qiniu;
    o && (r = o);
    var s = "8mb",
        l = !!t,
        d = 1,
        w = {
            Error: function (e, o, t) {
                console.error("qiniu upload error: ", e, o, t);
                try {
                    wgoo.$loading.hide()
                } catch (a) {}
                if (401 == o.status && d > 0) {
                    d--;
                    try {
                        console.info("-----------\x3e 重新获取七牛token"), e.init(), setTimeout((function () {
                            console.info("-----------\x3e 重新上传"), e.start()
                        }), 500)
                    } catch (a) {}
                } else o.code == plupload.FILE_SIZE_ERROR ? n && n.errorHandle ? n && n.errorHandle && n.errorHandle(o.code, o.message) : motify.show("所选图片不能超过".concat(s, ",视频不超过5mb")) : n && n.errorHandle ? n && n.errorHandle && n.errorHandle(o.code, o.message) : motify.show(t)
            },
            BeforeUpload: function (e, n) {}
        },
        u = $.extend({}, w, n),
        g = {
            size: "614400",
            width: 1024,
            height: 1024,
            crop: !1,
            quality: 92,
            preserve_headers: !1
        },
        p = $.extend({}, g, a || {}),
        f = r.uploader({
            runtimes: "html5",
            browse_button: e,
            uptoken_url: getAjaxUrl("/service/get_qiuniu_token.jsp"),
            uptoken: c,
            unique_names: !i,
            domain: "https://xcimg.szwego.com/",
            max_file_size: s,
            max_retries: 3,
            dragdrop: !0,
            drop_element: A,
            auto_start: !0,
            resize: p,
            filters: {
                mime_types: [{
                    title: "image",
                    extensions: "jpg,jpeg,png,bmp,webp"
                }, {
                    title: "video",
                    extensions: "mp4"
                }]
            },
            multi_selection: l,
            init: u
        });
    return f
};
var QiniuNum = 0,
    g_appUploadImgCB;
window.fileUploadInit = function (e, n, o, t, a, i, A) {
    var c = null;
    return QiniuNum > 0 && (c = new QiniuJsSDK), QiniuNum++, _fileUploadInit(e, n, c, o, t, a, i, A)
}, window.fileUploadMore = function (e, n, o, t, a, i, A) {
    return fileUploadInit(e, n, o, t, a, i, A)
}, window.parseURL = function (e) {
    var n = document.createElement("a");
    return n.href = e, n
}, 
window.getAjaxUrl = function (e) {
    var n = "https:",
        o = "appoffline:",
        t = "h5offline:",
        a = parseURL(e),
        i = a.host;
    return /^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$/.test(i) && (n = "http:"), 
    console.log("anchor.host, anchor.protocol: ", a.host, a.protocol), 
    a.protocol !== o && a.protocol !== t || (a.protocol = n, e = a.href), 
    console.log("url: ", e), 
    e
}, 
window.getUrlAddPara = function (e) {
    var n = getAjaxUrl(e);
    return getPar("client_type") && (n = setUrlParam(n, "client_type", getPar("client_type"))), getPar("token") && (n = setUrlParam(n, "token", getPar("token"))), getPar("version") && (n = setUrlParam(n, "version", getPar("version"))), getPar("channel") && (n = setUrlParam(n, "channel", getPar("channel"))), getPar("env") && (n = setUrlParam(n, "env", getPar("env"))), getPar("isKeyboardEnv") && (n = setUrlParam(n, "app_source", getPar("isKeyboardEnv"))), n
}, window._sensorBury = function (e) {
    e.sensorBury && "function" === typeof window.effectSensorBury && window.effectSensorBury(e.sensorBury)
}, window.getCookieByName = function (e) {
    for (var n = e + "=", o = document.cookie.split(";"), t = 0; t < o.length; t++) {
        var a = o[t].trim();
        if (0 == a.indexOf(n)) return a.substring(n.length, a.length)
    }
    return ""
}, window.getAppendHeader = function () {
    var e = getPar("client_type") || "net",
        n = getPar("version") || "",
        o = pcGetVersion(),
        t = getPar("js_header_albumid") || "",
        a = getPar("js_wego_uuid") || "",
        i = getPar("trackStaffId") || "",
        A = "0";
    if (isMobile.AppClient()) A = getPar("js_wego_staging") || "0";
    else {
        var c = "true" == getCookieByName("producte_run_to_dev_tomcat");
        A = c ? "1" : "0"
    }
    var r = {};
    return r = navigator.userAgent.match(/WegoAlbum/i) ? {
        "wego-albumid": t,
        version: o,
        "wego-staging": A,
        "wego-uuid": a,
        channel: "pc_client"
    } : {
        "wego-albumid": t,
        "wego-channel": e,
        "wego-version": n,
        "wego-staging": A,
        "wego-uuid": a
    }, i && (r["X-WG-TRACK-STAFF-ID"] = i), r
}, window.appendXTraceIdInfo = function (e, n) {
    var o = [9, 500],
        t = Number(e.errcode); - 1 != o.indexOf(t) && e.errmsg && (e.errmsg += "#$&" + n.getResponseHeader("X-Trace-Id"))
}, window.ajaxFn = function (e, n, o, t) {
    var a = !0;
    o && (a = !!o);
    var i = getUrlAddPara(e),
        A = getAppendHeader(),
        c = $.ajax({
            type: "get",
            dataType: "json",
            async: a,
            url: i,
            cache: !1,
            timeout: 38e3,
            headers: A,
            error: function (e, n, o) {
                console.log(e.readyState + e.status + e.responseText), console.log("XMLHttpRequest.responseText=" + e.responseText);
                var a = "网络有点堵，请稍后重试~";
                return motify.show(a), c.abort(), loadingImg.remove(), loading.remove(), e = null, t && "function" === typeof t && t(), !1
            },
            success: function (e, o, t) {
                if ("undefined" === typeof e) return loadingImg.remove(), loading.remove(), motify.show("数据异常,请稍后再试~"), !1;
                try {
                    "function" === typeof window._xhrSuccessHook && window._xhrSuccessHook({
                        url: i,
                        type: "get",
                        headers: A,
                        data: e,
                        resHeaders: t.getAllResponseHeaders(),
                        jqXHR: t
                    })
                } catch (a) {
                    console.error(a)
                }
                return _sensorBury(e), "undefined" === typeof e.errcode || 0 != e.errcode ? (loadingImg.remove(), loading.remove(), motify.show(e.errmsg), !1) : (e.token && isMobile.AppClient() && appShare(17, e.token, null, null), n && (console.log("callback"), n(e)), e = null, !1)
            },
            complete: function (e) {
                return null, !1
            }
        });
    return c
}, window.ajaxFnPost = function (e, n, o, t) {
    var a = getUrlAddPara(e),
        i = getAppendHeader(),
        A = $.ajax({
            type: "POST",
            url: a,
            data: o,
            traditional: !0,
            dataType: "json",
            timeout: 3e4,
            headers: i,
            error: function (e, n, o) {
                var a = window.navigator.onLine ? "网络有点堵，请稍后重试~" : "网络不可用~";
                return loadingImg.remove(), loading.remove(), t ? t(null, a) : motify.show(a), null, !1
            },
            success: function (e, o, A) {
                if ("undefined" === typeof e || "undefined" === typeof e.errcode) {
                    var c = "数据异常,请稍后再试~";
                    return loadingImg.remove(), loading.remove(), t ? t(null, c) : motify.show(c), !1
                }
                try {
                    "function" === typeof window._xhrSuccessHook && window._xhrSuccessHook({
                        url: a,
                        type: "post",
                        headers: i,
                        data: e,
                        resHeaders: A.getAllResponseHeaders(),
                        jqXHR: A
                    })
                } catch (r) {
                    console.error(r)
                }
                return _sensorBury(e), 0 != e.errcode ? (loadingImg.remove(), loading.remove(), t ? (appendXTraceIdInfo(e, A), t(e.errcode, e.errmsg, e.result)) : motify.show(e.errmsg), !1) : (e.token && isMobile.AppClient() && appShare(17, e.token, null, null), n && n(e), e = null, !1)
            }
        });
    return A
}, window.ajaxFnExt = function (e, n, o, t) {
    var a = !0;
    void 0 !== o && (a = o);
    var i = getUrlAddPara(e),
        A = getAppendHeader();
    console.log("ajax");
    var c = $.ajax({
        type: "get",
        dataType: "json",
        async: a,
        url: i,
        cache: !1,
        timeout: 38e3,
        headers: A,
        error: function (e, n, o) {
            if ("abort" != n) {
                loadingImg.remove(), loading.remove(), c.abort();
                var a = window.navigator.onLine ? "网络有点堵，请稍后重试~" : "网络不可用~";
                return t ? t(a) : motify.show(a), null, !1
            }
        },
        success: function (e, o, t) {
            if ("undefined" === typeof e) return loadingImg.remove(), loading.remove(), motify.show("数据异常,请稍后再试~"), !1;
            try {
                "function" === typeof window._xhrSuccessHook && window._xhrSuccessHook({
                    url: i,
                    type: "get",
                    headers: A,
                    data: e,
                    resHeaders: t.getAllResponseHeaders(),
                    jqXHR: t
                })
            } catch (a) {
                console.error(a)
            }
            return _sensorBury(e), n && (appendXTraceIdInfo(e, t), n(e)), e = null, !1
        },
        complete: function (e) {
            return null, !1
        }
    });
    return c
}, window.scrollSlideToggle = function (e, n) {
    var o = $(e),
        t = (n = n || "fast", 0),
        a = $(window).scrollTop(),
        i = 0;
    $(window).scroll((function () {
        t = a, a = $(this).scrollTop(), i = a - t, console.log("scrollDiff: ".concat(i)), i > 0 ? o.slideUp(n) : o.slideDown(n)
    }))
}, window.setHtmlTitle = function (e) {
    var n = $("body"),
        o = $('<iframe src="/static/image/icon_up.png" width="0" height="0" frameborder="no" border="0" ></iframe>');
    document.title = e, o.on("load", (function () {
        setTimeout((function () {
            o.off("load").remove()
        }), 0)
    })).appendTo(n), isMobile.WegoAlbumPC() && window.pcAction("pc_title", {
        title: e
    }), isMobile.AppClient() && 1 * getPar("version") < 2650 || saveTitle({
        title: e,
        location: location.hash
    })
}, window.saveTitle = function (e) {
    var n = e.location,
        o = e.title;
    GetDataFromSession("currTitleSessions", (function (t) {
        if (t) {
            t = JSON.parse(t);
            var a = t.location;
            if (a == n) return t.title = o, void SaveDataToSession("currTitleSessions", JSON.stringify(t))
        }
        t && SaveDataToSession("preTitleSessions", JSON.stringify(t)), SaveDataToSession("currTitleSessions", JSON.stringify(e))
    }))
}, window.SaveDataToSession = function (e, n) {
    isMobile.AppClient() ? SaveDataToApp(e, n) : sessionStorage.setItem(e, n)
}, window.GetDataFromSession = function (e, n) {
    if (isMobile.AppClient()) GetAppData(e, (function (e) {
        "function" === typeof n && n(e)
    }));
    else {
        var o = sessionStorage.getItem(e);
        "function" === typeof n && n(o)
    }
}, window._uploadImageWxFunc = function e(n, o, t, a, i, A, c, r) {
    _wx.uploadImage(t[o], 1, (function (s) {
        if (null != s) {
            r && r(n, i, t[o], 0, 0, s.toString());
            var l = i,
                d = getAjaxUrl("/service/upload_image_wx_to_qiniu.jsp"),
                w = {
                    serverId: s.toString()
                },
                u = getAppendHeader();
            $.ajax({
                type: "GET",
                url: d,
                data: w,
                headers: u,
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                success: function (e, a, i) {
                    try {
                        "function" === typeof window._xhrSuccessHook && window._xhrSuccessHook({
                            url: d,
                            type: "get",
                            headers: u,
                            reqData: w,
                            data: e,
                            resHeaders: i.getAllResponseHeaders(),
                            jqXHR: i
                        })
                    } catch (c) {
                        console.error(c)
                    }
                    0 == e.errcode ? (console.log("------data: 0xg: ", n, l, e.image7Url, e.width, e.height, s.toString()), A(n, l, e.image7Url, e.width, e.height, s.toString(), o, t.length)) : motify.show("上传图片失败")
                },
                error: function (e) {
                    alert(e)
                }
            })
        }
        o++, c && i++, o < a && e(n, o, t, a, i, A, c, r)
    }))
}, window.isUseWxUploadImage = function (e) {
    return !(!_wx.is_wx() && !_wx.isMiniapp()) && !(!isMobile.iOS() && !isMobile.Android())
}, window.javaUploadImgCB = function (e) {
    var n = JSON.parse(e),
        o = n.key;
    /^http/.test(o) || (o = "https://xcimg.szwego.com/".concat(n.key)), g_appUploadImgCB && g_appUploadImgCB(o, n.digital_watermark, n.w, n.h, n.view, n.index, n.total, n)
}, window.uploadImageFuncUploadId = function (e, n, o, t, a, i, A, c, r, s) {
    g_appUploadImgCB = c, _uploadImageFunc(e, n, o, t, a, i, A, !1, r, !1, s)
}, window.uploadImageFunc = function (e, n, o, t, a, i, A, c, r) {
    g_appUploadImgCB = c, _uploadImageFunc(e, n, o, t, a, i, A, !1, r)
}, window.uploadImageFuncNew = function (e, n, o, t, a, i, A, c, r, s) {
    g_appUploadImgCB = c, _uploadImageFunc(e, n, o, t, a, i, A, !0, r, s)
}, window._uploadImageFunc = function (e, n, o, t, a, i, A, c, r, s, l) {
    if (isUseWxUploadImage(i)) console.log("------- useWxUploadImage ---------"), _wx.chooseImage((function (c) {
        if (console.log(c), window.showWxUploadLoading && showWxUploadLoading(), null != c)
            if (c.length > 0)
                if (c.length + t <= o) {
                    var r = 0,
                        l = c.length;
                    _uploadImageWxFunc(e, r, c, l, n, a, i, A)
                } else s && s(), motify.show("图片最多".concat(o, "张~"));
        else s && s(), motify.show("亲,请选择图片哟~");
        else s && s(), motify.show("选取图片失败~")
    }), o - t, s);
    else {
        var d = {
            imgNum: o - t,
            uptoken: Qiniu.token
        };
        r && (d.type = r), "number" != typeof e && "string" != typeof e || (d.view = e), isMobile.AppClient() ? appShare(4, "undefined" === typeof l ? d : _objectSpread(_objectSpread({}, d), {}, {
            view: e
        }), null, null) : c || (i ? l ? ($("#".concat(l)).val(n), $("#".concat(l)).click()) : ($("#img_upload_mul").val(n), $("#img_upload_mul").click()) : ($("#img_upload").val(n), $("#img_upload").click()))
    }
};
var ReactFn = window.ReactFn = {},
    g_linkCallBack, g_catchHtmlShareGoods, tempFun;
if (ReactFn._pageRec = 0, ReactFn.comInfiniteScrollFn = function (e, n, o, t, a, i) {
        var A = e;
        $("#genericList").infinitescroll({
            itemsToLoad: "#genericList",
            section: a || 0,
            no_show_error: 1,
            path: function (e) {
                return ReactFn._pageRec = e, "".concat(n, "&page_index=").concat(e, "&search_value=").concat(encodeURI(encodeURI(A.state.filterText)))
            }
        }, (function (e) {
            if (loadingImg.remove(), e.token && isMobile.AppClient() && appShare(17, e.token, null, null), t) return t(e);
            if (0 == e.errcode) {
                if (o) return o(e)
            } else motify.show(e.errmsg)
        }), (function (e) {
            i && i(e)
        }))
    }, ReactFn.infiniteScrollClear = function (e, n) {
        $(window).unbind("scrollstop.infinitescroll"), e && n && ReactFn.setHistory(e, n)
    }, ReactFn.scrollSave = function (e, n) {
        $(window).unbind("scrollstop.infinitescroll");
        var o = "";
        if (n)
            for (var t = 0; t < n.length; t++) o = o + n[t] + (t == n.length - 1 ? "" : "&");
        window.sessionStorage.setItem(e, "".concat(getPageScrollTop(), "&").concat(ReactFn._pageRec)), "" != o && window.sessionStorage.setItem("".concat(e, "_data"), o), console.log("save:".concat(getPageScrollTop(), "&").concat(ReactFn._pageRec))
    }, ReactFn.scrollGet = function (e) {
        var n = window.sessionStorage.getItem("".concat(e, "_data"));
        return window.sessionStorage.removeItem("".concat(e, "_data")), n ? n.split("&") : []
    }, ReactFn.scrollBack = function (e) {
        var n = window.sessionStorage.getItem(e);
        if (n = n ? n.split("&") : [], console.log(n), !(n.length < 2)) {
            if (n[1] && ReactFn._pageRec < n[1]) return 99;
            window.sessionStorage.removeItem(e), 0 == getPageScrollTop() && 0 == parseInt(n[0]) || $("html, body").animate({
                scrollTop: parseInt(n[0])
            }, 0), console.log("success animate to history.....")
        }
    }, ReactFn.setSessionData = function (e) {
        for (var n in e) window.sessionStorage.setItem(n, e[n])
    }, ReactFn.getSessionData = function (e) {
        return window.sessionStorage.getItem(e)
    }, ReactFn.removeSessionData = function (e) {
        window.sessionStorage.removeItem(e)
    }, ReactFn.setHistory = function (e, n, o, t) {
        var a = {},
            i = getPageScrollTop(t),
            A = {
                page: ReactFn._pageRec,
                scrollTop: i,
                state: o || n.state
            };
        a[e] = JSON.stringify(A), ReactFn.setSessionData(a)
    }, ReactFn.getHistory = function (e) {
        var n = ReactFn.getSessionData(e);
        try {
            return n ? JSON.parse(n) : void 0
        } catch (o) {}
    }, ReactFn.toHistory = function (e) {
        var n = ReactFn.getHistory(e);
        if (n) {
            var o = n.scrollTop;
            return $("html, body").animate({
                scrollTop: o
            }, 0), document.body.scrollTop = o, console.log("success animate to history....."), o
        }
        return 0
    }, ReactFn.clearHistory = function (e) {
        ReactFn.removeSessionData(e)
    }, ReactFn.recoverHistory = function (e) {
        var n = ReactFn.toHistory(e);
        return ReactFn.clearHistory(e), n
    }, ReactFn.setLocalData = function (e, n) {
        for (var o in n = n ? "_".concat(n) : "", e) window.localStorage.setItem(o + n, e[o])
    }, ReactFn.getLocalData = function (e, n) {
        return n = n ? "_".concat(n) : "", window.localStorage.getItem(e + n)
    }, ReactFn.removeLocalData = function (e, n) {
        n = n ? "_".concat(n) : "", window.localStorage.removeItem(e + n)
    }, ReactFn.clearLocalData = function () {
        window.localStorage.clear()
    }, ReactFn.insertJs = function (e, n) {
        var o = document.createElement("div");
        o.id = "var_".concat(e);
        var t = document.createElement("script");
        t.type = "text/javascript", t.text = "var ".concat(e, " = ").concat(JSON.stringify(n)), o.appendChild(t), document.body.appendChild(o)
    }, ReactFn.removeJs = function (e) {
        var n = document.getElementById("var_".concat(e));
        n && document.body.removeChild(n)
    }, ReactFn.getJsVar = function (label) {
        var val = "";
        try {
            val = eval(label), ReactFn.removeJs(label)
        } catch (exception) {}
        return val
    }, ReactFn.AppPrintLog = function (e) {
        appShare(79, {
            type: "0",
            log: JSON.stringify(e)
        }), console.group && console.group("App Print Log"), console.log(e), console.groupEnd && console.groupEnd()
    }, ReactFn.AppWriteLog = function (e) {
        appShare(79, {
            type: "1",
            log: JSON.stringify(e)
        }), console.group && console.group("App Write Log"), console.log(e), console.groupEnd && console.groupEnd()
    }, window.linkForCallBack = function (e) {
        g_linkCallBack = e, appShare(8, "")
    }, window.CatchHtmlShareGoods = function (e) {
        g_catchHtmlShareGoods = e, appShare(12, "")
    }, window.linkResultCallBack = function (e) {
        appShare(9, e)
    }, window.JavaCallBack = function (e, n) {
        "9" == e ? g_linkCallBack && g_linkCallBack(n) : "12" == e ? g_catchHtmlShareGoods && g_catchHtmlShareGoods(n) : "101" == e && scrollTo(0, 0)
    }, window.appShare = function (e, n, o, t) {
        if (weixinPlat()) "function" === typeof o && o(n);
        else if (isMobile.AppAndroid()) window.native && "function" === typeof window.native.appclienShare && window.native.appclienShare(e, n ? JSON.stringify(n) : "");
        else if (isMobile.AppIOS()) {
            var a = {
                type: e,
                shareData: n ? JSON.stringify(n) : ""
            };
            console.warn("iosData:", a), window.webkit.messageHandlers.webViewApp.postMessage(a)
        } else "function" === typeof t ? t(n) : !(e > 3) && motify.show("请在手机中分享")
    }, window.openWeb = function (e) {
        if (e) {
            var n = navigator.userAgent.toLowerCase().match(/wego\/([\d.]+)/),
                o = n && n[1];
            if (console.log("linyj", o, e), !isMobile.WegoAlbumPC() || isNaN(parseFloat(o))) return window.location.href = e;
            var t = String(e).toUpperCase(),
                a = e,
                i = 0;
            if (i = a.match(/goods_edit\/((?!\/).)+(|\/)$/) ? 1 : a.match(/script\/edit(|\/)$/) ? 3 : 0, console.log("pcWinType", i), Number(o) >= 100 && 0 === i) return window.location.href = e;
            if (t.match(/^(\w+:\/\/)/)) return window.pcAction("open_web", {
                data: e,
                pcWinType: i
            });
            var A = window.location,
                c = [A.protocol, "//", A.hostname, A.port ? [":", A.port].join("") : ""].join("");
            if (t.startsWith("/")) {
                var r = new URL([c, e].join("")),
                    s = [r.protocol, "//", r.hostname, r.port ? [":", r.port].join("") : ""].join("");
                a = [s, r.pathname, r.search ? [r.search, "&_t="].join("") : "?_t=", Date.now(), r.hash].join("")
            }
            t.startsWith("?") && (a = [c, A.pathname, e].join("")), t.startsWith("#") && (a = [c, A.pathname, A.search ? [A.search, "&_t="].join("") : "?_t=", Date.now(), e].join("")), window.pcAction("open_web", {
                data: a,
                pcWinType: i
            })
        }
    }, window.pcGetVersion = function () {
        var e = navigator.userAgent.match(/wsxc_client_v_(\S*)_/);
        return console.log("pcGetVersion:" + e), e && e[1] || 0
    }, isMobile.WegoAlbumPC()) {
    var cefCustomObject, isCefSharp = !1;
    window.chrome && window.chrome.webview && window.chrome.webview.hostObjects ? cefCustomObject = window.chrome.webview.hostObjects.cefCustomObject : (cefCustomObject = cefSharpCustomObject, isCefSharp = !0), window.isMainPcWin = function () {
        var e = navigator.userAgent.toLowerCase().match(/wego\/([\d.]+)/);
        return null != e && e[1] >= 0 && e[1] < 200
    }, window.onCaptureUpdate = function (e) {
        e.show || "success" !== e.action || (pcAction("captcha", {}), location.reload())
    }, window.isSinglePcWin = function () {
        var e = navigator.userAgent.match(/wego\/([\d.]+)/);
        return null != e && (300 == e[1] || 310 == e[1])
    }, window.pcGoBack = function (e) {
        var n = window.history.length <= Math.abs(e);
        window.history.go(e), pcAction("close_win", {
            needCloseWin: n
        })
    }, window.pcAction = function (e, n) {
        if (console.log("pcAction:", e, n), "undefined" !== typeof cefCustomObject) {
            var o = navigator.userAgent.match(/wsxc_container_(\S*)_/);
            if ("object" == typeof n && o && (n.container = o[1] || ""), n = n || {}, isCefSharp && "object" == typeof n) {
                var t = navigator.userAgent.toLowerCase().match(/wego\/([\d.]+)/);
                n.container = null == t ? window.sessionStorage.getItem("_pc_container_c") : t[1]
            }
            console.log(e), console.log(n ? "string" == typeof n ? n : JSON.stringify(n) : ""), cefCustomObject.action(e, n ? "string" == typeof n ? n : JSON.stringify(n) : "")
        }
    }, window.pcGetData = function (e, n) {
        "undefined" !== typeof cefCustomObject ? isCefSharp ? cefCustomObject.getData(e, (function (e) {
            n(e)
        })) : cefCustomObject.getData(e).then(n) : n()
    }, window.pcSaveDataMem = function (e, n) {
        pcSaveData("mem", e, n)
    }, window.pcSaveDataLocalstorage = function (e, n) {
        pcSaveData("storage", e, n)
    }, window.pcSaveData = function (e, n, o) {
        "undefined" !== typeof cefCustomObject && cefCustomObject.saveData(e, n, o ? "string" == typeof o ? o : JSON.stringify(o) : "")
    }, window.pcCallJS = function (e, n) {
        console.log("pcCallJS---\x3e" + e + "," + n), window.postMessage({
            type: e,
            value: n
        }, "*")
    }, window.pcCallJSExt = function (e) {
        console.log("pcCallJSExt---\x3e", e);
        try {
            var n = e.replace(/\n/g, "\\n").replace(/\r/g, "\\r").replace(/\t/g, "\\t"),
                o = JSON.parse(n);
            window.postMessage(o, "*")
        } catch (t) {}
    }
}

function temp_fun() {
    "function" === typeof tempFun && tempFun()
}
window.appCall = function (e, n) {
        if (weixinPlat());
        else if (isMobile.AppAndroid()) native.appclienShare(e, JSON.stringify(n));
        else if (isMobile.AppIOS()) {
            var o = {
                type: e,
                shareData: JSON.stringify(n)
            };
            window.webkit.messageHandlers.webViewApp.postMessage(o)
        }
    }, window.connectWebViewJavascriptBridge = function (e) {
        if (window.WebViewJavascriptBridge) return e(WebViewJavascriptBridge);
        if (isMobile.AppIOS()) {
            if (window.WVJBCallbacks) return window.WVJBCallbacks.push(e);
            window.WVJBCallbacks = [e];
            var n = document.createElement("iframe");
            n.style.display = "none", n.src = "truedian://__BRIDGE_LOADED__", document.documentElement.appendChild(n), setTimeout((function () {
                document.documentElement.removeChild(n)
            }), 0)
        }
        document.addEventListener("WebViewJavascriptBridgeReady", (function () {
            e(WebViewJavascriptBridge)
        }), !1)
    }, $(document).ready((function () {
        connectWebViewJavascriptBridge((function (e) {
            e.registerHandler("functionInJs", (function (e, n) {
                if (console.log(e), e) {
                    var o = JSON.parse(e);
                    switch (o.type) {
                        case 1:
                            window.albumUpdateNosee ? (window.albumUpdateNosee(o.data), n(o.data)) : window.albumUpdateNoseeSave && (window.albumUpdateNoseeSave(o.data), n(o.data));
                            break;
                        case 2:
                            console.log("albumUpdateFollowed111"), window.albumUpdateFollowed && (console.log("albumUpdateFollowed333:".concat(o.data)), window.albumUpdateFollowed(o.data), window.albumUpdateNosee ? window.albumUpdateNosee(o.data) : window.albumUpdateNoseeSave && window.albumUpdateNoseeSave(o.data), n(o.data));
                            break;
                        case 3:
                            window.albumPullFetch && window.albumPullFetch();
                            break;
                        case 4:
                            window.albumUpdateShareTime && (window.albumUpdateShareTime(JSON.parse(o.data)), n(o.data));
                            break;
                        case 5:
                            window.albumUpdateTheme && (window.albumUpdateTheme(o.data), n(o.data));
                            break;
                        case 6:
                            window.albumDone && (window.albumDone(), n(o.data));
                            break;
                        case 7:
                            window.activityResume && window.activityResume(o.data), window.activityResumeForAddressClipboard && window.activityResumeForAddressClipboard(o.data), window.postMessage({
                                type: "onPageResume",
                                value: o.data
                            }, "*"), n(o.data);
                            break;
                        case 8:
                            window.getSearchImage && (window.getSearchImage(o.data), n(o.data));
                            break;
                        case 9:
                            window.confirmLeaveRoute && window.confirmLeaveRoute(o.data), window.confirmLeaveRouteForAddressClipboard && window.confirmLeaveRouteForAddressClipboard(o.data), n(o.data);
                            break;
                        case 10:
                            window.rigthTopMenu && window.rigthTopMenu(o.data), n(o.data);
                            break;
                        case 11:
                            window.getBleState && window.getBleState(o.data), n(o.data);
                            break;
                        case 12:
                            window.showShoppingCart && window.showShoppingCart(o.data), n(o.data);
                            break;
                        case 13:
                            window.scanCodeResult && window.scanCodeResult(o.data), n(o.data);
                            break;
                        case 14:
                            window.getKeyboardInputChange && window.getKeyboardInputChange(o.data), n(o.data);
                            break;
                        case 15:
                            window.keyboardBottomMenu && window.keyboardBottomMenu(o.data), n(o.data);
                            break;
                        case 16:
                            window.keyboardCrash && window.keyboardCrash(o.data), n(o.data);
                            break;
                        case 17:
                            window.keyboardContentChange && window.keyboardContentChange(o.data), n(o.data);
                            break;
                        case 18:
                            window.buryLogin && window.buryLogin(o.data), n(o.data);
                            break;
                        case 20:
                            window.getAppPageCacheData && window.getAppPageCacheData(o.data), n(o.data);
                            break;
                        case 21:
                            window.onAppPageHide && window.onAppPageHide(o.data), n(o.data);
                            break;
                        case 22:
                            window.delImageCallback && window.delImageCallback(o.data), n(o.data);
                            break;
                        case 23:
                            window.postMessage({
                                type: "onMenuAction",
                                value: o.data
                            }, "*"), n(o.data);
                            break;
                        case 24:
                            window.getAppTabsTip && window.getAppTabsTip(o.data);
                            break;
                        case 25:
                            window.getImageSearchLocalPath && (window.getImageSearchLocalPath(o.data), n(o.data));
                            break;
                        case 26:
                            window.getImageSearch7niuPath && (window.getImageSearch7niuPath(o.data), n(o.data));
                            break;
                        case 28:
                            window.resetSearchPageState && (window.resetSearchPageState(o.data), n(o.data));
                            break;
                        case 29:
                            window.notificationSearchPageImageSearch && (window.notificationSearchPageImageSearch(o.data), n(o.data));
                            break;
                        case 30:
                            window.postMessage({
                                type: "app_call_js_30",
                                value: o.data
                            }, "*"), n && n(o.data);
                            break;
                        case 31:
                            window.appUploadVideo && (window.appUploadVideo(o.data), n(o.data));
                            break;
                        case 32:
                            window.postMessage({
                                type: "app_call_js_32",
                                value: o.data
                            }, "*"), window.fileChooseCb && (window.fileChooseCb(o.data), n(o.data));
                            break;
                        case 500:
                            window.postMessage({
                                type: "keyboardInput",
                                value: o.data
                            }, "*"), n && n(o.data);
                            break;
                        default:
                            console.log("nativeData:default");
                            break
                    }
                }
            }))
        }))
    })), window.JSCallJava = function (e, n, o) {
        connectWebViewJavascriptBridge((function (t) {
            var a = {
                id: e,
                content: n
            };
            t.callHandler("callFromTDWeb", {
                param: a
            }, (function (e) {
                o(e)
            }))
        }))
    }, window.GetAppData = function (e, n) {
        JSCallJava("get_data", "js_".concat(e), n)
    }, window.GetSystemInfo = function (e) {
        isMobile.AppClient() && JSCallJava("get_system_info", "", (function (n) {
            if (n) {
                var o = JSON.parse(n);
                "function" === typeof e && e(o)
            }
        }))
    }, window.GetInputPhoneInfo = function (e) {
        isMobile.AppClient() && JSCallJava("get_input_phone_info", "", (function (n) {
            if (n) {
                var o = JSON.parse(n);
                "function" === typeof e && e(o)
            }
        }))
    }, window.getSystemPushAuthority = function (e) {
        isMobile.AppClient() && JSCallJava("get_system_pushAuthority", "", (function (n) {
            if (n) {
                var o = JSON.parse(n);
                "function" === typeof e && e(o)
            }
        }))
    }, window.getStatusBarHeight = function (e) {
        isMobile.AppClient() && JSCallJava("get_status_bar_height", "", (function (n) {
            n && "function" === typeof e && e(n)
        }))
    }, window.getSearchParams = function (e) {
        isMobile.AppClient() && JSCallJava("get_search_param", "", (function (n) {
            n && "function" === typeof e && e(n)
        }))
    }, window.getIosVersion = function () {
        try {
            return navigator.userAgent.match(/OS (\d+)_(\d+)_?(\d+)?/)[0].match(/(\d+)_(\d+)_?(\d+)?/g)[0].replace(/_/g, ".")
        } catch (e) {
            return "14.0.0"
        }
    }, window.JungleFixedBodyModel = function (e) {
        try {
            var n = ["10.0.1", "10.1", "10.2"];
            isMobile.iOS() && n.indexOf(getIosVersion()) > -1 ? "function" === typeof e && e(!0) : "function" === typeof e && e(!1)
        } catch (o) {
            e(!1)
        }
    }, window.SaveDataToApp = function (e, n, o) {
        if (o = "undefined" === typeof o || o, !isMobile.isAppInput() || "quit_ok" != e) {
            var t = {
                key: o ? "js_".concat(e) : e,
                value: n
            };
            appShare(34, t)
        }
    }, window.CustomAssign = function (e, n) {
        e = "[object Object]" == Object.prototype.toString.apply(e) ? e : {}, n = "[object Object]" == Object.prototype.toString.apply(n) ? n : {};
        for (var o in e) {
            var t = e[o],
                a = n[o];
            if ("[object Object]" == Object.prototype.toString.apply(t) && "[object Object]" == Object.prototype.toString.apply(a)) {
                if ("{}" == JSON.stringify(t)) {
                    e[o] = n[o];
                    continue
                }
                for (var i in t) a[i] && (t[i] = a[i])
            } else a && (e[o] = a)
        }
        return e
    }, console.warn("[V107 全局配置小程序Id] Come to Global Init Process"), window.GlobalConstant = {}, window.GlobalConstantFunc = function (e, n, o) {
        var t = null,
            a = null,
            i = {
                CustomerService: {
                    url: "",
                    miniappName: ""
                },
                seller: {},
                timeStamp: 0
            };
        o = o || i, i = CustomAssign(o, i);
        var A = window.localStorage.getItem("globalConstant");
        i = A ? CustomAssign(i, JSON.parse(A)) : i;
        var c = (new Date).getTime();
        c < i.timeStamp + 3e5 || (i.timeStamp = c, t = new Promise((function (n, o) {
            ajaxFn(e, (function (e) {
                0 == e.errcode && n(e.result)
            }), !0, (function (e) {
                o(void 0)
            }))
        })), a = new Promise((function (e, o) {
            ajaxFn(n, (function (n) {
                0 == n.errcode && e(n.result)
            }), !0, (function (e) {
                o(void 0)
            }))
        })), Promise.all([t.catch((function () {})), a.catch((function () {}))]).then((function (e) {
            i = CustomAssign(i, CustomAssign(e[0], e[1])), window.GlobalConstant = i, window.localStorage.setItem("globalConstant", JSON.stringify(i))
        })))
    }, GlobalConstantFunc.prototype.get = function (e) {
        if (window.GlobalConstant && window.GlobalConstant[e]) return window.GlobalConstant[e];
        var n = window.localStorage.getItem("globalConstant");
        return n ? (n = JSON.parse(n), n[e]) : void 0
    }, window.requestAnimationFrame = window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame || function (e) {
        return setTimeout(e, 1e3 / 60)
    }, window.cancelAnimationFrame = window.cancelAnimationFrame || window.webkitCancelAnimationFrame || window.webkitCancelRequestAnimationFrame || window.mozCancelAnimationFrame || clearTimeout,
    function () {
        window.compliance = {
            getState: function (e) {
                isMobile.AppIOS() ? GetAppData("ios_compliance", (function (n) {
                    if (n) try {
                        n = JSON.parse(n)
                    } catch (o) {}
                    "object" !== ("undefined" === typeof n ? "undefined" : _typeof(n)) && (n = null), n && n.res ? e(!0) : !n || !n.now || Date.now() - n.now > 18e4 ? e() : e(!1)
                })) : e(!0)
            },
            loadState: function (e) {
                isMobile.AppIOS() ? ajaxFnExt("/napi/album/config/ios_compliance/v1", (function (n) {
                    var o = n.errcode,
                        t = n.result;
                    if (0 === o) return SaveDataToApp("ios_compliance", JSON.stringify(t ? {
                        res: !0
                    } : {
                        now: Date.now()
                    })), void e(t);
                    e()
                }), !0, (function (n) {
                    console.log(n), e()
                })) : e(!0)
            }
        }
    }();