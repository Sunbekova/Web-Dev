"use strict";
var __esDecorate = (this && this.__esDecorate) || function (ctor, descriptorIn, decorators, contextIn, initializers, extraInitializers) {
    function accept(f) { if (f !== void 0 && typeof f !== "function") throw new TypeError("Function expected"); return f; }
    var kind = contextIn.kind, key = kind === "getter" ? "get" : kind === "setter" ? "set" : "value";
    var target = !descriptorIn && ctor ? contextIn["static"] ? ctor : ctor.prototype : null;
    var descriptor = descriptorIn || (target ? Object.getOwnPropertyDescriptor(target, contextIn.name) : {});
    var _, done = false;
    for (var i = decorators.length - 1; i >= 0; i--) {
        var context = {};
        for (var p in contextIn) context[p] = p === "access" ? {} : contextIn[p];
        for (var p in contextIn.access) context.access[p] = contextIn.access[p];
        context.addInitializer = function (f) { if (done) throw new TypeError("Cannot add initializers after decoration has completed"); extraInitializers.push(accept(f || null)); };
        var result = (0, decorators[i])(kind === "accessor" ? { get: descriptor.get, set: descriptor.set } : descriptor[key], context);
        if (kind === "accessor") {
            if (result === void 0) continue;
            if (result === null || typeof result !== "object") throw new TypeError("Object expected");
            if (_ = accept(result.get)) descriptor.get = _;
            if (_ = accept(result.set)) descriptor.set = _;
            if (_ = accept(result.init)) initializers.unshift(_);
        }
        else if (_ = accept(result)) {
            if (kind === "field") initializers.unshift(_);
            else descriptor[key] = _;
        }
    }
    if (target) Object.defineProperty(target, contextIn.name, descriptor);
    done = true;
};
var __runInitializers = (this && this.__runInitializers) || function (thisArg, initializers, value) {
    var useValue = arguments.length > 2;
    for (var i = 0; i < initializers.length; i++) {
        value = useValue ? initializers[i].call(thisArg, value) : initializers[i].call(thisArg);
    }
    return useValue ? value : void 0;
};
var __setFunctionName = (this && this.__setFunctionName) || function (f, name, prefix) {
    if (typeof name === "symbol") name = name.description ? "[".concat(name.description, "]") : "";
    return Object.defineProperty(f, "name", { configurable: true, value: prefix ? "".concat(prefix, " ", name) : name });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.ProductListComponent = void 0;
var core_1 = require("@angular/core");
var products_1 = require("../products");
var ProductListComponent = function () {
    var _classDecorators = [(0, core_1.Component)({
            selector: 'app-product-list',
            templateUrl: './product-list.component.html',
            styleUrls: ['./product-list.component.css'],
        })];
    var _classDescriptor;
    var _classExtraInitializers = [];
    var _classThis;
    var ProductListComponent = _classThis = /** @class */ (function () {
        function ProductListComponent_1() {
            this.products = products_1.products;
            this.searchInput = '';
        }
        Object.defineProperty(ProductListComponent_1.prototype, "filteredProducts", {
            get: function () {
                var searchTerm = this.searchInput.toLowerCase();
                return this.products.filter(function (product) { return product.name.toLowerCase().includes(searchTerm); });
            },
            enumerable: false,
            configurable: true
        });
        ProductListComponent_1.prototype.share = function (productName, productLink) {
            var shareMessage = "Check out this product: ".concat(productName, " - ").concat(productLink);
            var whatsappLink = "https://api.whatsapp.com/send?text=".concat(encodeURIComponent(shareMessage));
            window.location.href = whatsappLink;
        };
        ProductListComponent_1.prototype.sharetg = function (productName, productLink) {
            var shareMessage = "Check out this product: ".concat(productName, " - ").concat(productLink);
            var whatsappLink = "https://t.me/share/url?url=".concat(encodeURIComponent(shareMessage));
            window.location.href = whatsappLink;
        };
        ProductListComponent_1.prototype.nextImage = function (product) {
            if (product.img.length > 1) {
                product.currentImageIndex = (product.currentImageIndex + 1) % product.img.length;
            }
        };
        ProductListComponent_1.prototype.prevImage = function (product) {
            if (product.img.length > 1) {
                product.currentImageIndex =
                    (product.currentImageIndex - 1 + product.img.length) % product.img.length;
            }
        };
        return ProductListComponent_1;
    }());
    __setFunctionName(_classThis, "ProductListComponent");
    (function () {
        var _metadata = typeof Symbol === "function" && Symbol.metadata ? Object.create(null) : void 0;
        __esDecorate(null, _classDescriptor = { value: _classThis }, _classDecorators, { kind: "class", name: _classThis.name, metadata: _metadata }, null, _classExtraInitializers);
        ProductListComponent = _classThis = _classDescriptor.value;
        if (_metadata) Object.defineProperty(_classThis, Symbol.metadata, { enumerable: true, configurable: true, writable: true, value: _metadata });
        __runInitializers(_classThis, _classExtraInitializers);
    })();
    return ProductListComponent = _classThis;
}();
exports.ProductListComponent = ProductListComponent;
