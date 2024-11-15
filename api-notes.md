# API notes

## Get list of lists

https://auchandrive.lu/munsbach/module/mywishlist/action?action=getAllWishlist

```json
      "wishlists": [
        {
          "id_wishlist": "30880",
          "nbProducts": "4",
          "name": "Achats fréquents",
          "default": "0",
          "token": "A1E0839E246138BC",
          "isFrequentList": "1",
          "shareUrl": "https://auchandrive.lu/munsbach/module/mywishlist/view?token=A1E0839E246138BC",
          "listUrl": "https://auchandrive.lu/munsbach/module/mywishlist/view?id_wishlist=30880"
        }
      ]
```

## Create a list

```url
https://auchandrive.lu/munsbach/module/mywishlist/action?action=createNewWishlist&params[name]=test"
```

response:
```json
{"success":true,
"message":"La liste a \u00e9t\u00e9 correctement cr\u00e9\u00e9e",
"datas":{"name":"plop","id_wishlist":"39874"}}
```


## Add product to list

```url
https://auchandrive.lu/munsbach/module/mywishlist/action?
action=addProductToWishlist
params[id_product]=10383
params[idWishList]=39873
params[quantity]=1
params[id_product_attribute]=0"
```

## Does the user exist

https://auchandrive.lu/munsbach/module/mylogin/account?action=checkEmailForLogin

## authenticate

curl 'https://auchandrive.lu/munsbach/connexion' --data-raw 'back=&email=sonja.ugen%40gmail.com&password=NilsLior&submitLogin=1'

## wishlists

addListToCartUrl = "https:\/\/auchandrive.lu\/munsbach\/module\/mywishlist\/action?action=addListToCart";
editProductQtyUrl = "https:\/\/auchandrive.lu\/munsbach\/module\/mywishlist\/action?action=updateProductFromWishList";
removeFromWishlistUrl = "https:\/\/auchandrive.lu\/munsbach\/module\/mywishlist\/action?action=deleteProductFromWishlist";
wishlistAddProductToCartUrl = "https:\/\/auchandrive.lu\/munsbach\/module\/mywishlist\/action?action=addProductToCart";
wishlistUrl = "https:\/\/auchandrive.lu\/munsbach\/module\/mywishlist\/view";
createNewWishlistUrl = "https:\/\/auchandrive.lu\/munsbach\/module\/mywishlist\/action?action=createNewWishlist";

## urls

{
  "base_url": "https://auchandrive.lu/munsbach/",
  "current_url": "https://auchandrive.lu/munsbach/module/mywishlist/view?id_wishlist=30880",
  "shop_domain_url": "https://auchandrive.lu",
  "img_ps_url": "https://auchandrive.lu/munsbach/img/",
  "img_cat_url": "https://auchandrive.lu/munsbach/img/c/",
  "img_lang_url": "https://auchandrive.lu/munsbach/img/l/",
  "img_prod_url": "https://auchandrive.lu/munsbach/img/p/",
  "img_manu_url": "https://auchandrive.lu/munsbach/img/m/",
  "img_sup_url": "https://auchandrive.lu/munsbach/img/su/",
  "img_ship_url": "https://auchandrive.lu/munsbach/img/s/",
  "img_store_url": "https://auchandrive.lu/munsbach/img/st/",
  "img_col_url": "https://auchandrive.lu/munsbach/img/co/",
  "img_url": "https://auchandrive.lu/munsbach/themes/easyshopping/assets/img/",
  "css_url": "https://auchandrive.lu/munsbach/themes/easyshopping/assets/css/",
  "js_url": "https://auchandrive.lu/munsbach/themes/easyshopping/assets/js/",
  "pic_url": "https://auchandrive.lu/munsbach/upload/",
  "pages": {
    "address": "https://auchandrive.lu/munsbach/adresse",
    "addresses": "https://auchandrive.lu/munsbach/adresses",
    "authentication": "https://auchandrive.lu/munsbach/connexion",
    "cart": "https://auchandrive.lu/munsbach/panier",
    "category": "https://auchandrive.lu/munsbach/index.php?controller=category",
    "cms": "https://auchandrive.lu/munsbach/index.php?controller=cms",
    "contact": "https://auchandrive.lu/munsbach/nous-contacter",
    "discount": "https://auchandrive.lu/munsbach/reduction",
    "guest_tracking": "https://auchandrive.lu/munsbach/suivi-commande-invite",
    "history": "https://auchandrive.lu/munsbach/historique-commandes",
    "identity": "https://auchandrive.lu/munsbach/identite",
    "index": "https://auchandrive.lu/munsbach/",
    "my_account": "https://auchandrive.lu/munsbach/mon-compte",
    "order_confirmation": "https://auchandrive.lu/munsbach/confirmation-commande",
    "order_detail": "https://auchandrive.lu/munsbach/index.php?controller=order-detail",
    "order_follow": "https://auchandrive.lu/munsbach/suivi-commande",
    "order": "https://auchandrive.lu/munsbach/commande",
    "order_return": "https://auchandrive.lu/munsbach/index.php?controller=order-return",
    "order_slip": "https://auchandrive.lu/munsbach/avoirs",
    "pagenotfound": "https://auchandrive.lu/munsbach/page-introuvable",
    "password": "https://auchandrive.lu/munsbach/recuperation-mot-de-passe",
    "pdf_invoice": "https://auchandrive.lu/munsbach/index.php?controller=pdf-invoice",
    "pdf_order_return": "https://auchandrive.lu/munsbach/index.php?controller=pdf-order-return",
    "pdf_order_slip": "https://auchandrive.lu/munsbach/index.php?controller=pdf-order-slip",
    "prices_drop": "https://auchandrive.lu/munsbach/ps-promotions",
    "product": "https://auchandrive.lu/munsbach/index.php?controller=product",
    "search": "https://auchandrive.lu/munsbach/ps-recherche",
    "sitemap": "https://auchandrive.lu/munsbach/plan du site",
    "stores": "https://auchandrive.lu/munsbach/magasins",
    "supplier": "https://auchandrive.lu/munsbach/fournisseur",
    "register": "https://auchandrive.lu/munsbach/connexion?create_account=1",
    "order_login": "https://auchandrive.lu/munsbach/commande?login=1"
  },
  "alternative_langs": [],
  "theme_assets": "/munsbach/themes/easyshopping/assets/",
  "actions": { "logout": "https://auchandrive.lu/munsbach/?mylogout=" }
}
