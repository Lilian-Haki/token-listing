window.onload = () => {
    const inputs = document.querySelectorAll("input");

    inputs.forEach(input => {
        input.addEventListener('change', calculateLoan)
    })
}

function calculateLoan () {
    const investment = document.querySelector('#investment').value;
    const buyPrice = document.querySelector('#buyPrice').value;
    const sellPrice = document.querySelector('#sellPrice').value;
    const investmentFee = document.querySelector('#investmentFee').value;
    const exitFee = document.querySelector('#exitFee').value;

    if (!investment || !buyPrice || !sellPrice || !investmentFee || !exitFee ) return;

    const totalInvestment = investment
    //const totalexitAmount = (investment) * Math.pow(sellPrice / buyPrice) / investment
    //const profitLoss = totalexitAmount - totalInvestment
    //const monthlyInterest = interestRate / 100 / 12;
    //const emi = principal * monthlyInterest * Math.pow(1 + monthlyInterest, tenure) / (Math.pow(1 + monthlyInterest, tenure) - 1);

    //const totalAmount = emi * tenure;
    //const totalInterest = totalAmount - principal;

    //document.querySelector('#profitLoss').innerText = 'Profit/Loss: ' + profitLoss.toFixed(2);
    //document.querySelector('#totalInvestment').innerText = 'Total Investment: ' + totalInvestment.toFixed(2);
    //document.querySelector('#totalexitAmount').innerText = 'Total Exit Amount: ' + totalexitAmount.toFixed(2);
    document.querySelector('#profitLoss').innerText = totalInvestment.toFixed(2);

}