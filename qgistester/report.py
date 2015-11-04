class Report():

    def __init__(self):
        self.results = []

    def addTestResult(self, result):
        self.results.append(result)


class TestResult():

    PASSED, FAILED, SKIPPED = range(3)
    def __init__(self, test):
        self.test = test
        self.state = self.SKIPPED
        self.errorStep = None
        self.errorMessage = None

    def failed(self, step, message):
        self.status = self.FAILED
        self.errorStep = step
        self.errorMessage = message

    def passed(self):
        self.status = self.PASSED

    def skipped(self):
        self.status = self.SKIPPED

    def __str__(self):
        if self.status == self.SKIPPED:
            return "Test skipped"
        if self.status == self.PASSED:
            return "Test passed correctly"
        else:
            return "Test failed at step '%s' with message:\n%s" %(self.errorStep, self.errorMessage)