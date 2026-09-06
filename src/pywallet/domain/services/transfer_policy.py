from pywallet.domain.entities.wallet import Wallet

class TransferPolicy :


    @staticmethod
    def validate(
            source_wallet : Wallet,
            destination_wallet : Wallet,
            amount
        ):
        if not source_wallet.is_active :
            raise ValueError

        if not destination_wallet.is_active :
            raise ValueError

        if amount < 0 :
            raise ValueError

        if source_wallet.balance <= amount :
            raise ValueError