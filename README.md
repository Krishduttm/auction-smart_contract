# auction-smart_contract

Created an auction smart contract which runs for a specific zmount of seconds which can be changed. (in seconds)

Owner has to start the auction and anyone can start bidding by paying the smart contract, only higher bids are accepted and once the time runs out
bids are stopped.

Then the highest bidder function is called which returns the highest bidder and then for the sake of simplicity i added an implementation which transfers all the funds to the highest bidder. 

Implemented in brownie.
