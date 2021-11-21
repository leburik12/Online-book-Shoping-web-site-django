# class Number:
#     def __init__(self, val):
#         self.val = val
#     def __iadd__(self, other):
#         self.val += other
#         return self
# r = [1, 2, 3]
# x = Number(r)
# x += [4,5,6]
# x += [7,8,9]
# print(x.val)
# class Callee():
#     def __call__(self, *args, **kwargs):
#         print('Called: ')
# c = Callee()
# print(c(1, 2, 4))
# else:
#     words_of_category = category.split()
#     length_of_category_word = len(words_of_category)
#     if length_of_category_word >= 1:
#         for word in words_of_category:
#             all_books = all_books.filter(category__istartswith=word).values_list()
#             if all_books:
#                 message = 'success_db'
#                 break
#         if len(all_books.values()) <= 0:
#             message = 'not_found_db'
#     else:
#         message = 'not_found_db'
# for look_up_name, look_up_value in book_zenbil.items():
#     lookupvalue = look_up.get(look_up_name)
#     all_books = all_books.filter(**{lookupvalue:look_up_value})
# test = {}
# if test['3'] is  None:
#     print('eeeee')
# else:
#     print('ddd')
# t = 5
# print(t ,'%%%%%%%%%%%%%%')
# for look_up_name, look_up_value in book_zenbil.items():
#     lookupvalue = look_up.get(look_up_name)
#     all_books = all_books.filter( **{lookupvalue: look_up_value} )
# x = {'f': 43, 'f': 43}
# print(x)
# del x['f']
# print(x)
# for line in open('../admin.py'):
#     print(line.upper())  # calls __next__. catches StopIteration
# f = open('../admin.py')
# print(next(f))
# print(next(f))
# v = {'1': {
#     'product': {
#         'price': 4,
#         'qty': 8
#       }
#     },
#     '2': {
# 'product': {
#         'price': 5,
#         'qty': 8
#       }
# }
# }
# for p in v.values():     print(p)
# class Ma(object):
#     def __iter__(self):
#         it = [4, 9, 8]
#         for item in it:
#             yield (item)
# f = Ma()
# for a in f:
#     print(a)
# x = {'x': 1, 'y': 2, 'z': 3, 'a': 5}
# p = [4, 5, 9, 200]
# print(p.pop())
# class me:
#     def __init__(self, id):
#         self.my_id = id
#     def rr(self):
#         print(f'thisss{self.my_id}')
# f = me(4)
# f.rr()
# from decimal import Decimal
# x = '32.3'
# print(Decimal(x))

# class Indexer:
#     def __getitem__(self, item):
#         return item ** 2
#
# x = Indexer()
# print(x[10])
# <!--               {% if form.errors %}-->
# <!--                 {% for field in form %}-->
# <!--                       {% for error in field.errors %}-->
# <!--                         <div class="alert alert-danger">-->
# <!--                             <strong>-->
# <!--                                 {{ error|escape }}-->
# <!--                             </strong>-->
# <!--                         </div>-->
# <!--                       {% endfor %}-->
# <!--                       {% for error in form.non_field_errors %}-->
# <!--                        <div class="alert alert-danger">-->
# <!--                            <strong>-->
# <!--                                {{ error|escape }}-->
# <!--                            </strong>-->
# <!--                        </div>-->
# <!--                       {% endfor %}-->
# <!--                    {% endfor %}-->
# <!--               {% endif %}-->
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#                    <!--                     <div class="form-group">-->
# <!--                          <label>-->
# <!--                       Add Coupon ( if ) :-->
# <!--                       </label>-->
# <!--                       <input class="form-control" type="text" value="">-->
# <!--                   </div>-->
# <!--                    {% if object.new_book_hardcover_qty is not 0 %}-->
# <!--                                  <input  type="checkbox"> <span>New Book</span>-->
# <!--                                   <input class="form-control" type="number" min="0" max="{{ object.new_book_hardcover_qty }}" value="1"></span>-->
# <!--                          {% endif %}-->
# <!--                     <div>-->
# <!--                         <br>-->
# <!--                          {% if object.old_book_hardcover_qty is not 0 %}-->
# <!--                                   <span><input type="checkbox" > <span>Used Book</span>-->
# <!--                                   <input class="form-control" type="number" max="{{ object.old_book_hardcover_qty }}" min="0" value="0">-->
# <!--                           {% endif %}<br>-->
# <!--                                       {% if object.new_book_paperback_qty is not 0 %}-->
# <!--                                       <input  type="checkbox"> <span>Paper Back</span>-->
# <!--                                   <input class="form-control" type="number" min="0" max="{{object.new_book_paperback_qty}}" value="0"></span>-->
# <!--                              {% endif %}-->
# <!--                     </div>-->
# <!--                   <input type="text" name="override" value="false" hidden>-->
# <!--                   <p>+ $20 shipping</p>-->
# <!--                   <p>Total : $43.55</p>-->
# <!--                   <p>Arrives : Nov 23 - 90</p>-->














import re

t = 'cierneTruevomcwcw'

print(re.sub("\^True/", '', t))












