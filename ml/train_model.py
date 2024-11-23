from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# data
data = {
    "Hi": "Hello! How can I assist you today?",
    "Thank you": "You are welcome, feel free to ask any other question",
    "Got it thanks": "You are welcome, feel free to ask any other question",
    "What is your return policy?": "You can return any item within 30 days of purchase.",
    "How can I track my order?": "You can track your order using the tracking link sent to your email.",
    "What payment methods do you accept?": "We accept credit cards, PayPal, and other popular payment methods.",
    "Do you offer free shipping?": "Yes, we offer free shipping on orders over $50.",
    "What are your customer service hours?": "Our customer service team is available from 9 AM to 6 PM, Monday through Friday.",
    "Can I change my shipping address after placing an order?": "You can change your shipping address within 24 hours of placing your order by contacting our customer service.",
    "How do I cancel my order?": "To cancel your order, please contact our customer service team as soon as possible. If the order has not been shipped yet, we can cancel it for you.",
    "Do you ship internationally?": "Yes, we ship to many countries worldwide. Shipping costs and delivery times may vary based on your location.",
    "What is your refund policy?": "If you are not satisfied with your purchase, we offer a full refund within 30 days of purchase. Items must be in their original condition.",
    "How long does it take to process a refund?": "Refunds are typically processed within 5-7 business days after we receive your returned item.",
    "Can I exchange an item?": "Yes, we offer exchanges for items of equal value within 30 days of purchase.",
    "What is the warranty on your products?": "We offer a one-year warranty on all our products. If you encounter any issues, please contact our support team.",
    "How can I contact customer support?": "You can contact our customer support team via email at support@example.com or by phone at (123) 456-7890.",
    "Can I place an order over the phone?": "Yes, you can place an order over the phone by calling our sales team at (123) 456-7890.",
    "Do you have a physical store?": "We are primarily an online store, but we do have a few retail locations. Visit our website for a list of stores near you.",
    "How do I reset my account password?": "To reset your password, click on the 'Forgot Password' link on the login page and follow the instructions.",
    "What if I receive a damaged or defective item?": "If you receive a damaged or defective item, please contact our customer service immediately for a replacement or refund.",
    "Do you offer gift cards?": "Yes, we offer gift cards in various denominations. They can be purchased on our website.",
    "How do I redeem a discount code?": "You can redeem your discount code at checkout by entering it in the 'Promo Code' field.",
    "Can I add items to my order after it's been placed?": "Unfortunately, we cannot add items to an order once it's been placed. You can place a new order for additional items.",
    "Do you offer price matching?": "Yes, we offer price matching on select items. Please contact our customer service with details of the competitor's pricing.",
    "What if the item I want is out of stock?": "If an item is out of stock, you can sign up to be notified when it becomes available again.",
    "How do I know if my order was successful?": "After placing an order, you will receive a confirmation email with your order details.",
    "What are your shipping options?": "We offer standard, expedited, and overnight shipping options. You can choose your preferred method at checkout.",
    "How long does shipping take?": "Standard shipping typically takes 5-7 business days, while expedited shipping takes 2-3 business days. Overnight shipping is delivered the next day.",
    "Can I track my return?": "Yes, you can track your return using the tracking number provided when you initiate the return process.",
    "What should I do if I forget to apply a discount code?": "If you forgot to apply a discount code, please contact our customer service team, and they may be able to assist you.",
    "How can I update my billing information?": "You can update your billing information by logging into your account and editing your payment details.",
    "Can I preorder items?": "Yes, we offer preorder options on select items. You will be charged when the item ships.",
    "Do you offer customization or personalization of products?": "Yes, we offer customization on select products. Please check the product page for available options.",
    "How do I join your rewards program?": "You can join our rewards program by signing up on our website. Earn points for every purchase and redeem them for discounts.",
    "What if my package is lost during shipping?": "If your package is lost during shipping, please contact our customer service team, and we will assist in resolving the issue.",
    "Do you offer bulk discounts?": "Yes, we offer discounts on bulk orders. Please contact our sales team for more information.",
    "Can I return a gift?": "Yes, gifts can be returned for store credit or exchanged for another item of equal value.",
    "Are there any items that cannot be returned?": "Some items, such as personalized or final sale items, cannot be returned. Please check our return policy for details.",
    "How do I sign up for your newsletter?": "You can sign up for our newsletter by entering your email at the bottom of our homepage to receive updates and promotions.",
    "What is your policy on damaged items during shipping?": "If your item was damaged during shipping, please contact us immediately, and we will arrange for a replacement or refund.",
    "Can I combine multiple discount codes?": "Only one discount code can be applied per order. Discount codes cannot be combined.",
    "Do you offer gift wrapping?": "Yes, we offer gift wrapping services for an additional fee. You can select this option at checkout.",
    "How do I cancel my order?": "To cancel your order, please contact our customer service team as soon as possible. Once an order is processed, it may not be possible to cancel.",
    "What is the warranty on your products?": "We offer a one-year warranty on most of our products. Please check the specific product page for warranty details.",
    "Can I change my shipping address after placing an order?": "If your order hasn't shipped yet, you may be able to change the shipping address. Please contact customer service for assistance.",
    "Do you offer international shipping?": "Yes, we offer international shipping to select countries. Shipping costs and delivery times vary by location.",
    "How do I reset my account password?": "You can reset your password by clicking the 'Forgot Password' link on the login page and following the instructions.",
    "Can I purchase a gift card?": "Yes, we offer digital gift cards that can be sent via email. You can choose the value of the gift card at checkout.",
    "What is your exchange policy?": "We offer exchanges on most items within 30 days of purchase. Please visit our exchange page for instructions.",
    "How do I apply for a job at your company?": "You can view and apply for open positions on our careers page. We’re always looking for talented individuals to join our team.",
    "What should I do if I receive the wrong item?": "If you received the wrong item, please contact our customer service team, and we will resolve the issue by sending the correct item or issuing a refund.",
    "How can I check the balance on my gift card?": "You can check your gift card balance by entering the card number on our gift card balance page.",
    "Do you offer financing options?": "Yes, we offer financing options through our partner services. You can choose this option at checkout and apply for financing.",
    "How do I contact customer support?": "You can contact our customer support team via email, phone, or live chat. Visit our contact page for details.",
    "What is the minimum order amount for free shipping?": "Free shipping is available on orders over $50. This applies to standard shipping within the continental United States.",
    "Can I subscribe to product restock notifications?": "Yes, you can subscribe to restock notifications on the product page. We’ll notify you via email when the item is back in stock.",
    "How do I leave a review for a product?": "You can leave a review on the product page by clicking the 'Write a Review' button and submitting your feedback.",
    "Do you offer student discounts?": "Yes, we offer a discount for students. Please verify your student status through our student discount partner to receive a discount code.",
    "What happens if my payment is declined?": "If your payment is declined, please try a different payment method or contact your bank for assistance.",
    "Can I schedule a delivery for a specific date?": "We offer scheduled delivery on certain items. Please choose your preferred delivery date at checkout.",
    "What materials are your products made from?": "The materials vary by product. You can find detailed information on the materials used in each product on the product page.",
    "How can I make a bulk purchase?": "For bulk purchases, please contact our sales team for a customized quote and further assistance."

}


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data.keys())
y = list(data.values())

# model training
model = MultinomialNB()
model.fit(X, y)

# Saveing model and vectorizer
with open('chatbot_model.pkl', 'wb') as f:
    pickle.dump((model, vectorizer), f)
