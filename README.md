# Atomics

Sync from [swift-nio/CNIOAtomics](https://github.com/apple/swift-nio/tree/master/Sources/CNIOAtomics) and [swift-nio/NIOConcurrencyHelpers](https://github.com/apple/swift-nio/tree/master/Sources/NIOConcurrencyHelpers).

## usages

```swift
import Atomics

let n = NIOAtomic.makeAtomic(value: 0)
n.add(1)
n.sub(1)
_ = n.compareAndExchange(expected: 0, desired: 1)
_ = n.load()
```
