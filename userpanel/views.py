
from decimal import Decimal
from multiprocessing import context
from pprint import pprint
import random
from django.utils import timezone
import json
import time
from unittest import result
from django.core import serializers
from unicodedata import decimal, name
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template import RequestContext
from userpanel.models import Buychips, Member, Coderequest, Earning, Epin, Kyc, Transfer_records, Wallet, BetSingle, Widhdraw_requests, newlotteries, Result, newlotteriesnine, newlotteriesthreem, Resultthreem, Resultnine
from django.contrib.auth.hashers import make_password, check_password
from datetime import timedelta, datetime
from datetime import datetime
import datetime as dt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Min
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from collections import Counter
# from tronapi import Tron
from web3 import Web3
from web3.contract import Contract
# from web3 import Web3
# Create your views here.



def indexpage(request):
    return render(request, 'index.html')
    # return HttpResponse ("Lotto")


@login_required(login_url='/login')
def dashboard(request):
    

    
















    data = Member.objects.filter(username=request.user.username)
    wallet = Wallet.objects.get(username=request.user.username)
    bets = BetSingle.objects.filter(better = request.user.id).count()
    referrals = Member.objects.filter(sponsor = request.user).count()
    levelincome = Earning.objects.filter(username = request.user).count()
        
    return render(request,'dashboard.html', {'data': data, 'wallet':wallet, 'bets':bets, 'referrals':referrals, 'levelincome': levelincome})



def dividend(userid):
 
    try:
        data = Member.objects.get(userid=userid)
        if data.topupdate is not None:
            if data.staking == 24:
                dividend = 3
            if data.staking == 36:
                dividend = 4
            if data.staking == 48:
                dividend = 5
            if data.staking == 60:
                dividend = 6
            monthylydividend = float(data.topup) * dividend / 100
            perdaydividend = monthylydividend / 30    
            days = datetime.date.today() - data.topupdate

            return days.days * perdaydividend
        else:
            return True

    except Member.DoesNotExist:
        return 0


@login_required(login_url='/login')
def request_chips(request):
    if request.method=="POST":
        username = request.user.username
        hash_type = request.POST.get('type')
        hash = request.POST.get('hash')
        amount = request.POST.get('amount')
        if hash_type == "BUSD":
            mainabi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"_decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
            
            
            url = "https://bsc-dataseed.binance.org"
            web3 = Web3(Web3.HTTPProvider(url))

            receivingaddress = "TC89T4UPxztLsTCtfj67VXaErEXUYuwc3H"
            contract = web3.eth.contract(address=Web3.toChecksumAddress("0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"), abi= mainabi)
            result = web3.eth.get_transaction(hash)
            func_obj, func_params = contract.decode_function_input(result['input'])

            from_address = web3.toJSON(result['from'])
            to_address = func_params['recipient']
            busdamount = web3.fromWei(func_params['amount'], 'ether')
            print(amount)
            print(busdamount)
            
            exists = Buychips.objects.filter(hash=hash, amount=amount, username=username).exists()

            if exists == True:
                messages.error(request, 'Hash Already Exists. Please use another hash.')
                return redirect('/request_chips')
            elif int(amount) != int(busdamount):
                messages.error(request, 'Amount is not same. Please try again with same amount')
                return redirect('/request_chips')
            elif receivingaddress != to_address:
                messages.error(request, 'Invalid Hash')
                return redirect('/request_chips')
            else:
                try:
                    chips = web3.fromWei(func_params['amount'], 'ether') * 10
                    data = Buychips(username=username, type=hash_type, hash=hash, amount=amount, fromaddress = from_address, toaddress = to_address, chips = chips, status=1)
                    data.save()

                    receiverbalance = Wallet.objects.get(username=username)
                    receivertotal = int(receiverbalance.balance) + int(chips)            
                    Wallet.objects.filter(username = username).update(balance= receivertotal)
                    messages.success(request, 'Success')
                    return redirect('/request_chips')
        
                except:
                    messages.error(request, 'Request Not Submitted. Please try again')


                
                # print(web3.toJSON(result['status']))
                # print(web3.toJSON(result))
                # print(web3.toJSON(result['from']))
                # print(web3.toJSON(result['to']))
                # print(web3.toJSON(result['input']))
                
                # print(func_params['recipient'])
                # print(web3.fromWei(func_params['amount'], 'ether'))
        else:
            print("Type is USDT")
            return redirect('/request_chips')
            
    else:
      
        return render(request, 'request_code.html')
    


@login_required(login_url='/login')
def transfer_chips(request):
    if request.method=="POST":
        username = request.user.username
        amount = request.POST.get('amount')
        receiver = request.POST.get('receiver')        
        date = dt.datetime.now()
        
        if username == receiver:
            messages.error(request, 'Invalid Username')
            return redirect('/wallet')

        if amount =="":
            messages.error(request, 'Please Enter Proper Amount')
            return redirect('/wallet')
        if int(amount) < 20:
            messages.error(request, 'Minimum 20 Chips are required to Transfer')
            return redirect('/wallet')
        if receiver =="":
            messages.error(request, 'Please Enter Proper Receiver Username')
            return redirect('/wallet')
        userexists = Wallet.objects.filter(username=receiver).exists()

        if userexists == False:
            messages.error(request, 'Invalid Username')
            return redirect('/wallet')

        data = Wallet.objects.get(username=request.user)
        receiverbalance = Wallet.objects.get(username=receiver)
        print(receiverbalance.balance)

        if int(data.balance) < int(amount):
            messages.error(request, 'Insufficient Chips for Transfer')
            return redirect('/wallet')

        
        if int(data.balance) > int(amount):
            balanceamount = int(data.balance) - int(amount)
            receivertotal = int(receiverbalance.balance) + int(amount)            
        try:
            Wallet.objects.filter(username = request.user).update(balance= balanceamount)
            Wallet.objects.filter(username = receiver).update(balance= receivertotal)
            insert = Transfer_records(tousername= receiver, fromusername=request.user,amount=amount)
            insert.save()
            messages.success(request, 'Chips Transfered Successfully')
        except:
            messages.error(request, 'Request Not Submitted. Please try again')


       
        return redirect('/wallet')    

    else:
      
        return redirect('/wallet')





@login_required(login_url='/login')
def changepassword(request):
    if request.method=="POST":
        username = request.user.username
        oldpassword = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')        
        if oldpassword =="":
            messages.error(request, 'Please Enter Proper Password')
            return redirect('/changepassword')
        user = User.objects.get(username__exact=username)
        valid = user.check_password(oldpassword)
        
        if valid:
            newpassword = make_password(newpassword)
            User.objects.filter(username = username).update(password= newpassword)
            messages.success(request, 'Password Changed Successfully')
            return redirect('/changepassword')
        
        else:
            messages.error(request, 'Incorrect Old Password')
            return redirect('/changepassword')

    else:
        return render(request, 'profile/changepassword.html')

@login_required(login_url='/login')
def unused_codes(request):
    data = Epin.objects.filter(issue_to=request.user.username)
    context = {'username': request.user}
    return render(request, 'unused_codes.html', {'username': context, 'data': data})

@login_required(login_url='/login')
def mybets(request):
    data = BetSingle.objects.filter(better=request.user.id).order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
  

    context = {'username': request.user}
    return render(request, 'bets/mybets.html', {'username': context, 'users': users})


@login_required(login_url='/login')
def myearnings(request):
    data = BetSingle.objects.filter(better=request.user.id).order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
  

    context = {'username': request.user}
    return render(request, 'bets/mybets.html', {'username': context, 'users': users})


@login_required(login_url='/login')
def kyc(request):
    if request.method=="POST":
        id_proof = request.FILES['id_proof']
        address_proof = request.FILES['add_proof']
        photo = request.FILES['photo']        
        kyc = Kyc(userid= request.user.username, id_proof=id_proof, address_proof=address_proof, photo=photo)
        kyc.save()
        context = {'username': request.user}
        print(id_proof)
        data = Kyc.objects.filter(userid=request.user.username)
        return render(request, 'kyc/kyc.html', {'username': context, 'data':data})           

    else:
        data = Kyc.objects.filter(userid=request.user.username)
        context = {'username': request.user}
        return render(request, 'kyc/kyc.html', {'username': context, 'data':data})



# @login_required(login_url='/loginUser')
# def Profile(request):
#     #return render(request, 'profile/profile.html')
#     if request.method=="POST":
#         address = request.POST['address']
#         wallet_address = request.POST['wallet_address']
#         password = request.POST['oldpass']
#         tax_no = request.POST['tax_no']

#         profile_update = Member_profile.objects.filter(userid = request.user.username).update(
#             address=address,
#             taxnumber = tax_no,
#             walletaddress = wallet_address,
#         )

#         print(profile_update)
       
        
#         data = Member_profile.objects.filter(userid=request.user.username)
#         context = {'username': request.user}
#         return render(request, 'profile/profile.html', {'username': context, 'data':data})           

#     else:
        
#         data = Member_profile.objects.filter(userid=request.user.username)
#         print(data)
#         context = {'username': request.user}
#         return render(request, 'profile/profile.html', {'username': context, 'data':data})
    
    
    




def used_codes(request):
    return render(request, 'used_codes.html')

def obtain_earnings(request):
    data = Earning.objects.filter(userid=request.user.username)
    return render(request, 'earnings/obtain_earning.html', {'data': data})

def wallet(request):
    
    if request.method=="POST":        
        amount = request.POST['amount']
        if float(amount) < 10:
            messages.error(request, 'Invalid detail or some error. Please try again')
            return render(request, 'wallet/evacuate.html',{ 'wallet':wallet})
        else:
            for balance in wallet:
                if float(balance.balance) > float(amount):
                    restbalance = float(balance.balance) - float(amount)
                    Wallet.objects.filter(userid = request.user.username).update(balance= restbalance)
                    withdraw_enter = Widhdraw_requests(userid = request.user.username, amount = amount, date= datetime.date.today(), status='Pending')
                    withdraw_enter.save()
                    print(restbalance)
                    wallet = Wallet.objects.filter(userid=request.user.username)
                    return render(request, 'wallet/evacuate.html',{ 'wallet':wallet})

    else:
        wallet = Wallet.objects.get(username=request.user.username)
        return render(request, 'wallet/wallet.html', {'wallet': wallet})

@login_required(login_url='/login')
def with_request(request):
    
    if request.method=="POST":        
        amount = request.POST['amount']
        type = request.POST['type']
        walletaddress = request.POST['hash']
        if float(amount) < 10:
            messages.error(request, 'Amount Must Be  > 10')
            return redirect('/wallet')
        else:
            wallet = Wallet.objects.filter(username=request.user.username).values()
            for balance in wallet:
                if float(balance['balance']) > float(amount):
                    restbalance = float(balance['balance']) - float(amount)
                    Wallet.objects.filter(username = request.user.username).update(balance= restbalance)
                    withdraw_enter = Widhdraw_requests(username = request.user.username, wallet = walletaddress, amount = amount, date= dt.datetime.now(), type=type)
                    withdraw_enter.save()
                    print(restbalance)
                    messages.success(request, 'Request Submitted')
                    return redirect('/wallet')
                
                else:
                    messages.error(request, 'Balance is Low')
                    return redirect('/wallet')
    else:
        return redirect('/wallet')


@login_required(login_url='/login')
def accounting(request):

    data = Member.objects.filter(username=request.user.username)
    wallet = Wallet.objects.get(username=request.user.username)
    bets = BetSingle.objects.filter(better = request.user.id).count()
    winning = BetSingle.objects.filter(better = request.user.id, status="Win").count()
    lost = BetSingle.objects.filter(better = request.user.id, status="Lost").count()
    referrals = Member.objects.filter(sponsor = request.user).count()
    levelincome = Earning.objects.filter(username = request.user).count()
    totalbetsamount = BetSingle.objects.filter(better= request.user.id).aggregate(Sum('amount'))
    betsum = totalbetsamount["amount__sum"]

    totalwinning = BetSingle.objects.filter(better= request.user.id, status="Win").aggregate(Sum('amount'))
    sumwinning = totalwinning["amount__sum"]

    totallost = BetSingle.objects.filter(better= request.user.id, status="Lost").aggregate(Sum('amount'))
    sumlost = totallost["amount__sum"]

    totalearn = Earning.objects.filter(username= request.user.username).aggregate(Sum('amount'))
    totearning = totalearn["amount__sum"]

    print(betsum)  
    return render(request,'wallet/accounting.html', {'data': data, 'wallet':wallet, 'bets':bets, 'winning': winning, 'lost': lost, 'totalbetsamount': betsum, 'sumwinning': sumwinning, 'sumlost': sumlost,'referrals':referrals, 'levelincome': levelincome, 'earning':totearning})


def loginUser(request):
    
    if request.method=="POST":        
        username = request.POST['username']
        password =  request.POST['password']     
        print(username)
        user = authenticate(request, username=username, password=password)
        
        # return HttpResponse (user)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, 'Invalid detail. Please try again')
            return render(request, 'login.html')
    
    else:
        return render(request, 'login.html')



def logoutUser(request):
    logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect("/login")

def validate_username(request):
    sponsor = request.GET.get('sponsor', None)
    data = {
        'is_taken': Member.objects.filter(userid=sponsor).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

def register(request):
    
    if request.method=="POST":
        sponsor = request.POST.get('sponsor')
        # username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        usertype = request.POST.get('type')
        password = request.POST.get('password')
        userid= random.randint(234567895, 992345678)
        join_date = dt.datetime.now()
        status = 'Not Active'

        print(name)

        try:
            is_taken = User.objects.filter(username=userid).exists()
            if is_taken == True:
                messages.error(request, 'UserID Already Exists.')
                return render(request, 'register.html')
            else:               

                # sponsortype = Member.objects.get(username=sponsor)
                # print(sponsortype.type)

                # if usertype == '5' and sponsortype.type != '5':

                #     messages.error(request, 'Sponsor is Not a Super User')
                #     return render(request, 'register.html')

                # if usertype != '5' and sponsortype.type == '5':

                #     messages.error(request, 'Sponsor is Not a Normal User')
                #     return render(request, 'register.html')

                
                data = Member(username = userid, userid = userid, join_date= join_date,  status = status, name=name, email=email, sponsor = sponsor, phone = phone, type=usertype)
                data.save()

                user = User(username=userid, email=email, last_login=dt.datetime.now())
                user.set_password(password)
                user.save()

                walletEntry = Wallet(username = userid,  balance = 0)
                walletEntry.save()


                return render(request, 'referrals/success.html', {'name': name, 'username': userid, 'sponsor':sponsor})
        
        except Exception as e:
            print(e)
            messages.error(request, 'Invalid Sponsor or some error. Please try again')
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')

def add_user_byagent(request):
    if request.method=="POST":
        sponsor = request.user
        # username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        userid= random.randint(234567895, 992345678)
        join_date = dt.datetime.now()
        status = 'Not Active'

        print(name)

        try:
            is_taken = User.objects.filter(username=userid).exists()
            if is_taken == True:
                messages.error(request, 'Username Already Exists.')
                return render(request, 'referrals/add_user.html')
            else:
                user = User(username=userid, email=email, last_login=dt.datetime.now())
                user.set_password(password)
                user.save()
                
                data = Member(username = userid,userid = userid, join_date= join_date,  status = status, name=name, email=email, sponsor = sponsor, phone = phone, type="agent_user")
                data.save()

                walletEntry = Wallet(username = userid,  balance = 0)
                walletEntry.save()


                return render(request, 'referrals/panelsuccess.html', {'name': name, 'username': userid, 'sponsor':sponsor})
        
        except Exception as e:
            print(e)
            messages.error(request, 'Invalid detail or some error. Please try again')
            return render(request, 'referrals/add_user.html')

    else:
        return render(request, 'referrals/add_user.html')



def add_agent(request):
    if request.method=="POST":
        sponsor = request.user
        # username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        userid= random.randint(234567895, 992345678)
        join_date = dt.datetime.now()
        status = 'Not Active'

        print(name)

        try:
            is_taken = User.objects.filter(username=userid).exists()
            if is_taken == True:
                messages.error(request, 'Username Already Exists.')
                return render(request, 'referrals/add_agent.html')
            else:
                user = User(username=userid, email=email, last_login=dt.datetime.now())
                user.set_password(password)
                user.save()
                
                data = Member(username = userid,userid = userid, join_date= join_date,  status = status, name=name, email=email, sponsor = sponsor, phone = phone, type="3")
                data.save()

                walletEntry = Wallet(username = userid,  balance = 0)
                walletEntry.save()


                return render(request, 'referrals/panelsuccess.html', {'name': name, 'username': userid, 'sponsor':sponsor})
        
        except Exception as e:
            print(e)
            messages.error(request, 'Invalid detail or some error. Please try again')
            return render(request, 'referrals/add_agent.html')

    else:
        return render(request, 'referrals/add_agent.html')


def add_distributor(request):
    
    if request.method=="POST":
        sponsor = request.user
        # username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        userid= random.randint(234567895, 992345678)
        join_date = dt.datetime.now()
        status = 'Not Active'

        print(name)

        try:
            is_taken = User.objects.filter(username=userid).exists()
            if is_taken == True:
                messages.error(request, 'Username Already Exists.')
                return render(request, 'referrals/add_distributor.html')
            else:
                user = User(username=userid, email=email, last_login=dt.datetime.now())
                user.set_password(password)
                user.save()
                
                data = Member(username = userid,userid = userid, join_date= join_date,  status = status, name=name, email=email, sponsor = sponsor, phone = phone, type="2")
                data.save()

                walletEntry = Wallet(username = userid,  balance = 0)
                walletEntry.save()


                return render(request, 'referrals/panelsuccess.html', {'name': name, 'username': userid, 'sponsor':sponsor})
        
        except Exception as e:
            print(e)
            messages.error(request, 'Invalid detail or some error. Please try again')
            return render(request, 'referrals/add_distributor.html')

    else:
        return render(request, 'referrals/add_distributor.html')



def add_user_from_panel(request):
    
    if request.method=="POST":
        sponsor = request.user
        # username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        userid= random.randint(234567895, 992345678)
        join_date = dt.datetime.now()
        status = 'Not Active'

        print(name)

        try:
            is_taken = User.objects.filter(username=userid).exists()
            if is_taken == True:
                messages.error(request, 'Username Already Exists.')
                return render(request, 'referrals/add_user_panel.html')
            else:
                
                data = Member(username = userid,userid = userid, join_date= join_date,  status = status, name=name, email=email, sponsor = sponsor, phone = phone, type="4")
                data.save()

                user = User(username=userid, email=email, last_login=dt.datetime.now())
                user.set_password(password)
                user.save()

                walletEntry = Wallet(username = userid,  balance = 0)
                walletEntry.save()


                return render(request, 'referrals/panelsuccess.html', {'name': name, 'username': userid, 'sponsor':sponsor})
        
        except Exception as e:
            print(e)
            messages.error(request, 'Invalid detail or some error. Please try again')
            return render(request, 'referrals/add_user_panel.html')

    else:
        return render(request, 'referrals/add_user_panel.html')

def my_referrals(request):
    context = {'username': request.user}
    data = Member.objects.filter(sponsor=request.user)
    return render(request, 'referrals/my_referrals.html', {'username': context,'data':data})

def levelearning(request):
    data = Earning.objects.filter(username=request.user)
    return render(request, 'earnings/levelearnings.html', {'data':data})

def chips_bought(request):
    data = Buychips.objects.filter(username=request.user.username)
    return render(request, 'wallet/chips_bought.html', {'data':data})

def transfer_records(request):
    data = Transfer_records.objects.filter(fromusername=request.user.username)
    return render(request, 'wallet/transfer_records.html', {'data':data})


def check_business(userid, i=0):
    data = Member.objects.filter(sponsor=userid)
    countdata = Member.objects.filter(sponsor = userid).aggregate(Sum('topup'))
    if countdata["topup__sum"] is not None:
        i += countdata["topup__sum"]
   
    for d in data:
        if d.userid is not None:

            i = check_business(d.userid, i)

    return i



def new_ticket(request):
    return render(request, 'support/new_ticket.html')

def all_tickets(request):
    return render(request,'support/all_tickets.html')

def topup_account(request):
    if request.method == "POST":
        # level = (20,15,10,10,5,5,5,5,5,5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,)
        level = (5,3,2,1,1)
        
        pin = request.POST.get('topup')
        try:
            pindetail = Epin.objects.get(epin=pin)
            Epin.objects.filter(epin = pin).update(status = 'used', used_by=request.user.username, used_time=datetime.datetime.now())
            
            if pindetail.amount >= 50 and pindetail.amount < 500:
                dividendamount = 3
            if pindetail.amount >= 500 and pindetail.amount < 1000:
                dividendamount = 4
            if pindetail.amount >= 1000 and pindetail.amount < 5000:
                dividendamount = 5
            if pindetail.amount >= 50000:
                dividendamount = 6
            
            Member.objects.filter(userid = request.user.username).update(dividend=dividendamount, topup = float(pindetail.amount), status="Active", topupdate = datetime.datetime.now())
            #print(pindetail.amount)
            sponsor = Member.objects.filter(userid=request.user.username).values_list('sponsor', flat=True)
            fspon = ""
            i = 0
            for spn in sponsor:
                fspon = spn           
                
                for sp in level:
                    
                    if(i == 0):                
                        main_sponsor = fspon                
                    else:
                        main_sponsor = find_level_sponsor(main_sponsor, i)

                        # print(main_sponsor, sp)
                    if main_sponsor is not None:
                        if(sp > 0 ) and (main_sponsor > 0):
                            # print(main_sponsor, sp)
                            # print("pay")
                            pay_earning(main_sponsor, pindetail.amount * sp/100, 'Level Income', i , request.user.username, 'Pending', datetime.datetime.now())
                            print(main_sponsor, sp)
                    
                    i += 1
            
        except Epin.DoesNotExist:
            print("Not Found")
        return redirect('/dashboard')

    else:
        return redirect('/dashboard')


def find_level_sponsor(sponsor, i):

    if (i > 0):
        spon = Member.objects.filter(userid=sponsor).values_list("sponsor", flat=True)
        if spon is None:
            return None
        else:
            i =- 1
            for sponmain in spon:
                if sponmain is not None:
                    return find_level_sponsor(sponmain, i)
    else:
        return sponsor



def pay_earning(username, amount, type, levels, ref_id, status):

    balance = Wallet.objects.filter(username=username).values()
    for b in balance:
        print(b['level_earning'])
        Wallet.objects.filter(username=username).update(balance= float(b['balance']) + float(amount))  

    data = Earning(username = username, amount=amount, type= type, levels=levels, ref_id=ref_id,status = status, date=dt.datetime.now())
    data.save()


    # Wallet.objects.filter(username=username).update(level_earning= balance.level_earning + amount)
    # bal = int(wallet.level_earning) + int(amount)
    # Wallet.objects.filter(username = username).update(level_earning = bal)
    return True

# def pay_dividend(userid, amount, date, status):
#     data = Dividend(userid = userid, amount=amount, date=date, status = status)
#     data.save()
#     return True


# def closing(request):   
#     allmembers = Member.objects.all()
#     for members in allmembers:
#         if members.topup >0:
#             if members.dividend is not None:
#                 d0 = members.topupdate
#                 d1 = datetime.datetime.now().date()
#                 delta = d1 - d0
                
#                 dividend = members.topup * members.dividend / 100
#                 perday = dividend / 7
#                 roi = round(delta.days * perday, 2)
#                 print(roi)
                
#                 if roi > 0.00:
#                     totdividend = Dividend.objects.filter(userid = members.userid).aggregate(Sum('amount'))
                   
#                     if totdividend["amount__sum"] is None:
#                         totdivi = round(0,2)
#                     else:
#                         totdivi = round(totdividend["amount__sum"],2)
                   
#                     if roi > totdivi:
#                         mainroi = roi - totdivi
#                         print(mainroi)
#                         if mainroi > 0.00:
#                             pay_dividend(members.userid, mainroi, datetime.datetime.now(), 'Pending')
#                             pay_level_roi(members.userid,mainroi)
        
#     return HttpResponse ("closing done")
    

def pay_level_roi(userid,roiamount):
    level = (20,15,10,10,5,5,5,5,5,5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5,2.5)
    sponsor = Member.objects.filter(userid=userid).values_list('sponsor', flat=True)
    #print(sponsor)
    fspon = ""
    i = 0
    for spn in sponsor:
        fspon = spn           
        
        for sp in level:
            
            if(i == 0):                
                main_sponsor = fspon                
            else:
                main_sponsor = find_level_sponsor(main_sponsor, i)

                # print(main_sponsor, sp)
            if main_sponsor is not None:
                if(sp > 0 ) and (main_sponsor > 0):
                    # print(main_sponsor, sp)
                    # print("pay")
                    pay_earning(main_sponsor, roiamount * sp/100, 'Roi Level Income', i , userid, 'Pending', datetime.datetime.now())
                    # print(main_sponsor, roiamount*sp/100)
                
            i += 1
    return True



# def paylevelmaintype(lottotype, usertype, period, gametype, betnumber, evenorodd, amount, username, lastresult, userid):
#     # print("paylevelmaintype called Now")
#     divide = 5
#     multiply = 9

#     if (lastresult % 2) == 0:
#         resultevenorodd = "Even"
#     else:
#         resultevenorodd = "Odd"

#     if betnumber == lastresult:
#         BetSingle.objects.filter(period=period, better = userid, number= betnumber).update(winnningamount= amount * 9,status='Win')
        
#     else:
#         BetSingle.objects.filter(period=period, better = userid, number= betnumber).update(status='Lost')
        
#         pay_level_amount_maintype(userid,amount, period, username, usertype)
    
    
#     return True



# def paylevel(lottotype,period, userid, lastresult):
       
#     betdata = BetSingle.objects.filter(period=period, better=userid).values()
    
    
#     # if betnumber == lastresult:
#     #     BetSingle.objects.filter(period=period, better = userid, number= betnumber).update(winnningamount= amount * 9,status='Win')
        
#     # else:
#     #     BetSingle.objects.filter(period=period, better = userid, number= betnumber).update(status='Lost')
    
#     # pay_level_amount(userid,amount, period, username)
    
#     # if gametype == 'multi':
#     #     if evenorodd == resultevenorodd:
#     #         BetSingle.objects.filter(period=period, better = userid, evenorodd= evenorodd).update(winnningamount= amount / divide * multiply, status='Win')
#     #     else:
#     #         BetSingle.objects.filter(period=period, better = userid, evenorodd= evenorodd).update(status='Lost')
        
#     #     pay_level_amount(userid,amount, period, username)
    
#     return True


def pay_level_amount(amount, period, username):
    # print("paylevelamount called")
    level = (2, 1.5, 1, 0.50, 0.50, 0.50, 0.50, 0.25, 0.25, 0.25, 0.25)
    # sponsor = Member.objects.filter(userid=userid).values_list('sponsor', flat=True)
    spon = Member.objects.filter(userid=username).values_list('sponsor', flat=True)
    fspon = ""
    i = 0
    for spn in spon:
        fspon = spn           
        
        for sp in level:
            
            if(i == 0):                
                main_sponsor = fspon                
            else:
                main_sponsor = find_level_sponsor(main_sponsor, i)

                # print(main_sponsor, sp)
            if main_sponsor is not None:
                if(float(sp) > 0.00 ) and (int(main_sponsor) > 0.00):
                    # print(main_sponsor, sp)
                    # print("pay")
                    pay_earning(main_sponsor, amount * sp/100, 'Level Income', i , period, 'Pending')
                    print(main_sponsor, sp)
            
            i += 1
    # i = 0             
        
    # for sp in level:
        
    #     if(i == 0):                
    #         main_sponsor = spon.sponsor                
    #     else:
    #         main_sponsor = find_level_sponsor(spon.sponsor, i)

    #         # print(main_sponsor, sp)
    #     if main_sponsor is not None:
    #         if(sp is not None ) and (main_sponsor is not None):
    #             # print(main_sponsor, sp)
    #             # print("pay")
    #             pay_earning(main_sponsor, amount * sp/100, 'Level Income', i , period, 'Pending')
    #             # print(main_sponsor, sp)
        
    #     i += 1
    
    return True


def pay_level_amount_maintype(amount, period, username, usertype):
    spon = Member.objects.filter(userid=username).values_list('sponsor', flat=True)
    fspon = ""
    i = 1
    
    for spn in spon:
        
        fspon = spn
        spontype = Member.objects.get(username=username)
        stype= int(spontype.type)
        
        if (stype == 1):
            sendlevel = ()
            # lev = (7.5,)
            # print(lev)

        elif (stype == 2):
            sendlevel = (7.5,)

        elif (stype == 3):
            sendlevel = (5, 2.5,)
        
        elif (stype == 4):
            sendlevel = (2.5, 2.5, 2.5,)

        else:
            sendlevel()

        print("Spon type is ", stype)
        print("Send level is ", sendlevel)  

        for sp in sendlevel:
            
            if(i == 1):                
                main_sponsor = fspon                
            else:
                main_sponsor = find_level_sponsor(main_sponsor, i)

                # print(main_sponsor, sp)
            if main_sponsor is not None:
                if(float(sp) > 0.00 ) and (int(main_sponsor) > 0.00):
                    # print(main_sponsor, sp)
                    # print("pay")
                    pay_earning(main_sponsor, amount * sp/100, 'Level Income', i , period, 'Pending')
                    print(main_sponsor, sp)
            
            i += 1
    # print("paylevelmaintype called")
    # spon = Member.objects.filter(userid=username).values_list('sponsor', flat=True)
    
    # spontype = Member.objects.get(username=spon)
    # print(spontype)
    
    # if spontype.type == "1":
    #     sendlevel = (7.5,)
    # else:
    #     sendlevel = ()
    # if spontype.type == "2":
    #     sendlevel = (7.5,)
    # else:
    #     sendlevel = ()
        
    # if spontype.type == "3":
    #     sendlevel = (5, 2.5,)
    # else:
    #     sendlevel = ()  
    
        
    # if spontype.type == "panel":
    #     sendlevel = (2.5, 2.5, 2.5,)
    # else:
    #     sendlevel = ()
    
    
    # fspon = ""
    # i = 0
    # for spn in spon:
    #     fspon = spn           
        
    #     for sp in sendlevel:
            
    #         if(i == 0):                
    #             main_sponsor = fspon                
    #         else:
    #             main_sponsor = find_level_sponsor(main_sponsor, i)

    #             # print(main_sponsor, sp)
    #         if main_sponsor is not None:
    #             if(float(sp) > 0.00 ) and (int(main_sponsor) > 0.00):
    #                 # print(main_sponsor, sp)
    #                 # print("pay")
    #                 pay_earning(main_sponsor, amount * sp/100, 'Level Income', i , period, 'Pending')
    #                 print(main_sponsor, sp)
            
    #         i += 1
    
    return True

def sendpayments(period, lottotype, timing, resultno):
    
    # period = 2070
    # resultno = 6
    # lotterydata = lottotype.objects.get(id=period)
    betdata = BetSingle.objects.filter(period=period, timing=timing).values()
    for b in betdata:
        # bet_user = int(b['better'])
        bet_user = User.objects.get(id=b['better'])
        bet_id = int(b['id'])
        amount = int(b['amount'])
        usertype = Member.objects.get(username=bet_user.username)
        print("User Type", usertype.type)

        if resultno == int(b['number']):
            balance = Wallet.objects.filter(username=bet_user.username).values()
            for b in balance:
                print(b['balance'])
                Wallet.objects.filter(username=bet_user.username).update(balance= float(b['balance']) + float(amount * 9))            
            BetSingle.objects.filter(period=period, better = bet_user.id, number= resultno, id=bet_id).update(winnningamount= amount * 9,status='Win')
        else:
            BetSingle.objects.filter(period=period, better = bet_user.id, id=bet_id).update(status='Lost')

        if (usertype.type == '1'):
            pay_level_amount_maintype(amount, period, bet_user.username, usertype)
        elif (usertype.type == '2'):
            pay_level_amount_maintype(amount, period, bet_user.username, usertype)
        elif (usertype.type == '3'):
            pay_level_amount_maintype(amount, period, bet_user.username, usertype)
        elif (usertype.type == '4'):
            pay_level_amount_maintype(amount, period, bet_user.username, usertype)

            #  or (usertype.type == 2) or (usertype.type == 3) or (usertype.type == 'panel'):
            # print("called")
            
       
        else:
            print("called Pay Level Earning")
            pay_level_amount(amount, period, bet_user.username)
    
    return True
    


        # print(numbers)
        # uname = User.objects.get(id=b['better'])
        # usertype = Member.objects.get(username=uname.username)
        # # print(b['number'], b['amount'])
        
        # if usertype.type == 1 or usertype.type == 2 or usertype.type == 3 or usertype.type == 'panel':
        #     paylevelmaintype(lottotype, usertype.type, period, b['type'], b['number'], b['evenorodd'], b['amount'], uname.username, resultno, b['better'])
        # else:
        #     paylevel(lottotype, period, uname.username, resultno)
       
    
def sendpayments99(period, lottotype, timing, resultno):
    # period = 2070
    # resultno = 6
    # lotterydata = lottotype.objects.get(id=period)
    betdata = BetSingle.objects.filter(period=period, timing=timing).values()
    for b in betdata:
        # bet_user = int(b['better'])
        bet_user = User.objects.get(id=b['better'])
        bet_id = int(b['id'])
        amount = int(b['amount'])
        usertype = Member.objects.get(username=bet_user.username)

        if resultno == int(b['number']):
            balance = Wallet.objects.filter(username=bet_user.username).values()
            for b in balance:
                print(b['level_earning'])
                Wallet.objects.filter(username=bet_user.username).update(balance= float(b['balance']) + float(amount * 90))            
            BetSingle.objects.filter(period=period, better = bet_user.id, number= resultno, id=bet_id).update(winnningamount= amount * 90,status='Win')
        else:
            BetSingle.objects.filter(period=period, better = bet_user.id, id=bet_id).update(status='Lost')

        if usertype.type == 1 or usertype.type == 2 or usertype.type == 3 or usertype.type == 'panel':
            pay_level_amount_maintype(amount, period, bet_user.username, usertype)
       
        else:
            pay_level_amount(amount, period, bet_user.username)
    
    return True
    
def sendresult(period, lottotype, type):
    # period = 2070
    # type = 3
    resnumber = "none"
    betamount={}
    allnumberswithmin ={}
    for number in range(10):
        betdata = BetSingle.objects.filter(period=period, timing=type, number=number).aggregate(Sum('amount'))
        if betdata["amount__sum"] is not None:
            betamount[number] = betdata["amount__sum"]
        if betdata["amount__sum"] is None:
            betamount[number] = 0
    smallnumber = min(betamount.values())
    minvaluenumber = min(betamount, key=betamount.get)
    sumbetamount = sum(betamount.values())
    res = sum(x == smallnumber for x in betamount.values())
    print(res)
    if res > 1:
        for key, value in betamount.items():
            if value == smallnumber:
                allnumberswithmin[key] = value
                
        resnumber = random.choice(list(allnumberswithmin))    
    elif sumbetamount == 0:
        resnumber = random.choice(list(betamount))
    else:
       resnumber = minvaluenumber
    print(betamount)
    print("Minimum Value", smallnumber)
    print("Minimum Value Number", resnumber)
    print("Sum Bet Amount", sumbetamount)
    
    return resnumber

    

def sendresult99(period, lottotype, type):
    # period = 2070
    # type = 3
    resnumber = "none"
    betamount={}
    allnumberswithmin ={}
    for number in range(99):
        betdata = BetSingle.objects.filter(period=period, timing=type, number=number).aggregate(Sum('amount'))
        if betdata["amount__sum"] is not None:
            betamount[number] = betdata["amount__sum"]
        if betdata["amount__sum"] is None:
            betamount[number] = 0
    smallnumber = min(betamount.values())
    minvaluenumber = min(betamount, key=betamount.get)
    sumbetamount = sum(betamount.values())
    res = sum(x == smallnumber for x in betamount.values())
    print(res)
    if res > 1:
        for key, value in betamount.items():
            if value == smallnumber:
                allnumberswithmin[key] = value
                
        resnumber = random.choice(list(allnumberswithmin))    
    elif sumbetamount == 0:
        resnumber = random.choice(list(betamount))
    else:
       resnumber = minvaluenumber
    print(betamount)
    print("Minimum Value", smallnumber)
    print("Minimum Value Number", resnumber)
    print("Sum Bet Amount", sumbetamount)
    
    return resnumber



def addlotteryadmin(request):
    time.sleep(30)
    lastlottery = newlotteries.objects.count()
  
    
    if lastlottery <= 0:
        result_3 = timezone.now() + timedelta(minutes=15)
        add = newlotteries(created_at=timezone.now(), created_by="Admin", expired_at=result_3, price=random.randint(20500, 40000))
        add.save()     
        return HttpResponse("Done")
    

    alldata = newlotteries.objects.get(id=lastlottery)
    if alldata.status =='open':
        resultno = sendresult(lastlottery, newlotteries, 15)
        sendpay = sendpayments(lastlottery, newlotteries, 15, resultno)
        # resultno = random.randint(0,9)
        result = Result(period=alldata.id, created_at=alldata.created_at, result=resultno, status="close", price=random.randint(20500, 40000))
        result.save()
        newlotteries.objects.filter(id=alldata.id).update(status='close')

        lastlottery1 = newlotteries.objects.last().id
        alldata1 = newlotteries.objects.get(id=lastlottery1)
        if alldata1.status =='close':
            print("Period", alldata1.id)
            print("Created Time", alldata1.created_at)
            print("Expired Time", alldata1.expired_at)
            delta = alldata1.expired_at - timezone.now() 

            print("difference:", delta.total_seconds())
            time.sleep(delta.total_seconds())
            now = timezone.now()
            result_3 = now + timedelta(minutes=15)
        
            add = newlotteries(created_at=now, created_by="Admin", expired_at=result_3, price=random.randint(20500, 40000))
            add.save()     
            return HttpResponse("Done")
    else:
        now = timezone.now()
        result_3 = now + timedelta(minutes=15)
    
        add = newlotteries(created_at=now, created_by="Admin", expired_at=result_3, price=random.randint(20500, 40000))
        add.save()     
        return HttpResponse("Done")
    
    return HttpResponse("Error")


def addlotteryadmin3m(request):
    time.sleep(30)
    lastlottery = newlotteriesthreem.objects.count()
    # print(lastlottery)
    
    if lastlottery <= 0:
        result_3 = timezone.now() + timedelta(minutes=3)
        add = newlotteriesthreem(created_at=timezone.now(), created_by="Admin", expired_at=result_3, price=random.randint(20500, 40000))
        add.save()     
        return HttpResponse("Done")

    alldata = newlotteriesthreem.objects.get(id=lastlottery)
    if alldata.status =='open':
        resultno = sendresult(lastlottery, newlotteriesthreem, 3)
        sendpay = sendpayments(lastlottery, newlotteriesthreem, 3, resultno)
        result = Resultthreem(period=alldata.id, created_at=alldata.created_at, result=resultno, status="close", price=random.randint(20500, 40000))
        result.save()
        newlotteriesthreem.objects.filter(id=alldata.id).update(status='close')

        lastlottery1 = newlotteriesthreem.objects.last().id
        alldata1 = newlotteriesthreem.objects.get(id=lastlottery1)
        if alldata1.status =='close':
            print("Period", alldata1.id)
            print("Created Time", alldata1.created_at)
            print("Expired Time", alldata1.expired_at)
            delta = alldata1.expired_at - timezone.now() 

            print("difference:", delta.total_seconds())
            time.sleep(delta.total_seconds())
            now = timezone.now()
            result_3 = now + timedelta(minutes=3)
        
            add = newlotteriesthreem(created_at=now, created_by="Admin", expired_at=result_3, price=random.randint(20500, 40000))
            add.save()     
            return HttpResponse("Done")
    else:
        now = timezone.now()
        result_3 = now + timedelta(minutes=3)
    
        add = newlotteriesthreem(created_at=now, created_by="Admin", expired_at=result_3, price=random.randint(20500, 40000))
        add.save()     
        return HttpResponse("Done")
    
    return HttpResponse("Error")

def addlotteryadmin99(request):
    time.sleep(30)
    lastlottery = newlotteriesnine.objects.count()
    print(lastlottery)
    
    if lastlottery <= 0:
        result_3 = timezone.now() + timedelta(minutes=10)
        add = newlotteriesnine(created_at=timezone.now(), created_by="Admin", expired_at=result_3, price=random.randint(20500, 40000))
        add.save()     
        return HttpResponse("Done")

    alldata = newlotteriesnine.objects.get(id=lastlottery)
    if alldata.status =='open':
        resultno = sendresult99(lastlottery, newlotteriesnine, 10)
        sendpay = sendpayments99(lastlottery, newlotteriesnine, 10, resultno)
        
        result = Resultnine(period=alldata.id, created_at=alldata.created_at, result=resultno, status="close", price=random.randint(20500, 40000))
        result.save()
        newlotteriesnine.objects.filter(id=alldata.id).update(status='close')

        lastlottery1 = newlotteriesnine.objects.last().id
        alldata1 = newlotteriesnine.objects.get(id=lastlottery1)
        if alldata1.status =='close':
            print("Period", alldata1.id)
            print("Created Time", alldata1.created_at)
            print("Expired Time", alldata1.expired_at)
            delta = alldata1.expired_at - timezone.now() 

            print("difference:", delta.total_seconds())
            time.sleep(delta.total_seconds())
            now = timezone.now()
            result_3 = now + timedelta(minutes=10)
        
            add = newlotteriesnine(created_at=now, created_by="Admin", expired_at=result_3, price=random.randint(20500, 40000))
            add.save()     
            return HttpResponse("Done")
    else:
        now = timezone.now()
        result_3 = now + timedelta(minutes=10)
    
        add = newlotteriesnine(created_at=now, created_by="Admin", expired_at=result_3, price=random.randint(20500, 40000))
        add.save()     
        return HttpResponse("Done")
    
    return HttpResponse("Error")


def getlottery(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            lastlottery = newlotteries.objects.last().id
            alldata = newlotteries.objects.get(id=lastlottery)
            resdata1 = Result.objects.all().order_by('-id')[:5]
            resdata = serializers.serialize('json', resdata1)
            lastresult = Result.objects.last().id
            singleresultdata1 = Result.objects.get(id=lastresult)
         
            return JsonResponse({'id':alldata.id, 'expired_at':alldata.expired_at, 'resdata':resdata, 'lastresult':singleresultdata1.result, 'price': alldata.price})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return JsonResponse('Invalid request')

def getlottery3m(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            lastlottery = newlotteriesthreem.objects.last().id
            alldata = newlotteriesthreem.objects.get(id=lastlottery)
            resdata1 = Resultthreem.objects.all().order_by('-id')[:5]
            resdata = serializers.serialize('json', resdata1)
            lastresult = Resultthreem.objects.last().id
            singleresultdata1 = Resultthreem.objects.get(id=lastresult)
           
            
            return JsonResponse({'id':alldata.id, 'expired_at':alldata.expired_at, 'resdata':resdata, 'lastresult':singleresultdata1.result, 'price':alldata.price})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return JsonResponse('Invalid request')


def getlottery99(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'GET':
            lastlottery = newlotteriesnine.objects.last().id
            alldata = newlotteriesnine.objects.get(id=lastlottery)
            resdata1 = Resultnine.objects.all().order_by('-id')[:5]
            resdata = serializers.serialize('json', resdata1)
            lastresult = Resultnine.objects.last().id
            singleresultdata1 = Resultnine.objects.get(id=lastresult)
           
            
            return JsonResponse({'id':alldata.id, 'expired_at':alldata.expired_at, 'resdata':resdata, 'lastresult':singleresultdata1.result, 'price': alldata.price})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return JsonResponse('Invalid request')


def getresult(request):

    res = Result.objects.all().order_by('-id')[:10]
    for r in res:
        print(r.result)
    return HttpResponse("Done")

def getresult3m(request):

    res = Resultthreem.objects.all().order_by('-id')[:10]
    for r in res:
        print(r.result)
    return HttpResponse("Done")

def getresult99(request):

    res = Resultnine.objects.all().order_by('-id')[:10]
    for r in res:
        print(r.result)
    return HttpResponse("Done")


def placebet(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            
            data = json.load(request)
            userid = data.get('uid')
            amt = data.get('amt')
            betperiod = data.get('period')
            type = data.get('type')
            timinglottery = data.get('timing')
            now = datetime.today()
            print(amt)
            wallet = Wallet.objects.get(username=request.user.username)
            print(wallet.balance)
            
            if int(wallet.balance) < int(amt):
                return JsonResponse({'status':'0'})
            else:
                bal = int(wallet.balance) - int(amt)
                Wallet.objects.filter(username = request.user.username).update(balance = bal)

            if type == "Even":
                divideamount = int(amt) / 5
                for number in range(10):
                    if number % 2 == 0:
                        add = BetSingle(amount=divideamount, number=number, period=betperiod,better=userid, type="multi", status="pending",timing=timinglottery, created_at=now)
                        add.save()
                return JsonResponse({'status':'success'})

            if type == "Odd":
                divideamount = int(amt) / 5
                for number in range(10):
                    if number % 2 != 0:
                        add = BetSingle(amount=divideamount, number=number, period=betperiod,better=userid, type="multi", status="pending",timing=timinglottery, created_at=now)
                        add.save()
                return JsonResponse({'status':'success'})

            else:
                add = BetSingle(amount=amt, number=type,period=betperiod,better=userid, type="single", status="pending", timing=timinglottery, created_at=now)
                add.save()            
                return JsonResponse({'status':'success'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return JsonResponse('Invalid request')




def placebet99(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            
            data = json.load(request)
            userid = data.get('uid')
            amt = data.get('amt')
            betperiod = data.get('period')
            type = data.get('type')
            timinglottery = data.get('timing')
            now = datetime.today()
            print(amt)
            wallet = Wallet.objects.get(username=request.user.username)
            print(wallet.balance)
            
            if int(wallet.balance) < int(amt):
                return JsonResponse({'status':'0'})
            else:
                bal = int(wallet.balance) - int(amt)
                Wallet.objects.filter(username = request.user.username).update(balance = bal)

            if type == "Even":
                divideamount = int(amt) / 50
                for number in range(99):
                    if number % 2 == 0:
                        add = BetSingle(amount=divideamount, number=number, period=betperiod,better=userid, type="multi", status="pending",timing=timinglottery, created_at=now)
                        add.save()
                return JsonResponse({'status':'success'})

            if type == "Odd":
                divideamount = int(amt) / 50
                for number in range(99):
                    if number % 2 != 0:
                        add = BetSingle(amount=divideamount, number=number, period=betperiod,better=userid, type="multi", status="pending",timing=timinglottery, created_at=now)
                        add.save()
                return JsonResponse({'status':'success'})

            else:
                add = BetSingle(amount=amt, number=type,period=betperiod,better=userid, type="single", status="pending", timing=timinglottery, created_at=now)
                add.save()            
                return JsonResponse({'status':'success'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return JsonResponse('Invalid request')


def lotteryresult(request):
    lastlottery = newlotteries.objects.last().id
    lotterystatus = newlotteries.objects.get(id=lastlottery)
    if lotterystatus.status =='open':
        total = BetSingle.objects.filter(type = "").aggregate(Sum('amount'))
    print(data)
    if(total is not None):
        totearn = total["amount__sum"]
    else:
        totearn = 0.0
        data = BetSingle.objects.filter(period=lastlottery)
        for d in data:
            print(d.type)

    return HttpResponse("result")



@login_required(login_url='/login')
def result15m(request):
    data = Result.objects.all().order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 300)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
  

    context = {'username': request.user}
    return render(request, 'results/results15m.html', {'username': context, 'users': users})


@login_required(login_url='/login')
def result3m(request):
    
    data = Resultthreem.objects.all().order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 300)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
  

    context = {'username': request.user}
    return render(request, 'results/result3m.html', {'username': context, 'users': users})

@login_required(login_url='/login')
def result99(request):
    
    data = Resultnine.objects.all().order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(data, 300)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
  

    context = {'username': request.user}
    return render(request, 'results/result99m.html', {'username': context, 'users': users})



def playgame(request):
    wallet = Wallet.objects.get(username=request.user.username)
    return render(request, 'playgame/playgame.html', {'wallet':wallet})

def playgame3m(request):
    wallet = Wallet.objects.get(username=request.user.username)
    return render(request, 'playgame/playgame3m.html', {'wallet':wallet})

def playgame99(request):
    wallet = Wallet.objects.get(username=request.user.username)
    return render(request, 'playgame/playgame99.html', {'wallet':wallet})