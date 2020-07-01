import XCTest
@testable import Atomics

final class AtomicsTests: XCTestCase {
    func testExample() {
        let n = NIOAtomic.makeAtomic(value: 0)
        n.add(1)
        n.sub(1)
        _ = n.compareAndExchange(expected: 0, desired: 1)
        _ = n.load()
    }

    static var allTests = [
        ("testExample", testExample),
    ]
}
