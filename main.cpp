#include <behaviortree_cpp/bt_factory.h>
#include <iostream>
#include <thread>
#include <chrono>

//USED AI TO Config and understand 
// Run in the terminal via comman : ".\build\Debug\bt_main.exe"


// ------------------ Move towards room door ------------------
class MoveTowardsDoorRoom : public BT::SyncActionNode {
public:
    MoveTowardsDoorRoom(const std::string& name, const BT::NodeConfiguration& config)
    : BT::SyncActionNode(name, config) {}
    BT::NodeStatus tick() override {
        std::cout << "Moving towards the door of the room" << std::endl;
        return BT::NodeStatus::SUCCESS;
    }
    static BT::PortsList providedPorts() { return {}; }
};

// ------------------ Check Room Door ------------------
class CheckRoomDoorClosed : public BT::SyncActionNode {
public:
    CheckRoomDoorClosed(const std::string& name, const BT::NodeConfiguration& config)
    : BT::SyncActionNode(name, config), door_closed_(false) {}
    BT::NodeStatus tick() override {
        std::cout << "Checking if ROOM door is closed: " << (door_closed_ ? "Yes" : "No") << std::endl;
        return door_closed_ ? BT::NodeStatus::SUCCESS : BT::NodeStatus::FAILURE;
    }
    void setDoorClosed(bool closed) { door_closed_ = closed; }
    static BT::PortsList providedPorts() { return {}; }
private:
    bool door_closed_;
};

// ------------------ Open Door ------------------
class OpenDoor : public BT::SyncActionNode {
public:
    OpenDoor(const std::string& name, const BT::NodeConfiguration& config)
    : BT::SyncActionNode(name, config) {}
    BT::NodeStatus tick() override {
        std::cout << "Opening the door" << std::endl;
        return BT::NodeStatus::SUCCESS;
    }
    static BT::PortsList providedPorts() { return {}; }
};

// ------------------ Enter Room ------------------
class EnterRoom : public BT::SyncActionNode {
public:
    EnterRoom(const std::string& name, const BT::NodeConfiguration& config)
    : BT::SyncActionNode(name, config) {}
    BT::NodeStatus tick() override {
        std::cout << "Entering the room" << std::endl;
        return BT::NodeStatus::SUCCESS;
    }
    static BT::PortsList providedPorts() { return {}; }
};

// ------------------ Move towards fridge door ------------------
class MoveTowardsFridgeDoor : public BT::SyncActionNode {
public:
    MoveTowardsFridgeDoor(const std::string& name, const BT::NodeConfiguration& config)
    : BT::SyncActionNode(name, config) {}
    BT::NodeStatus tick() override {
        std::cout << "Moving towards the door of the fridge" << std::endl;
        return BT::NodeStatus::SUCCESS;
    }
    static BT::PortsList providedPorts() { return {}; }
};

// ------------------ Check Fridge Door ------------------
class CheckFridgeDoorClosed : public BT::SyncActionNode {
public:
    CheckFridgeDoorClosed(const std::string& name, const BT::NodeConfiguration& config)
    : BT::SyncActionNode(name, config), fridge_closed_(false) {}
    BT::NodeStatus tick() override {
        std::cout << "Checking if FRIDGE door is closed: " << (fridge_closed_ ? "Yes" : "No") << std::endl;
        return fridge_closed_ ? BT::NodeStatus::SUCCESS : BT::NodeStatus::FAILURE;
    }
    void setFridgeClosed(bool closed) { fridge_closed_ = closed; }
    static BT::PortsList providedPorts() { return {}; }
private:
    bool fridge_closed_;
};

// ------------------ Find Apple ------------------
class FindApple : public BT::SyncActionNode {
public:
    FindApple(const std::string& name, const BT::NodeConfiguration& config)
    : BT::SyncActionNode(name, config), apple_present_(true) {}
    BT::NodeStatus tick() override {
        std::cout << "Looking for an apple: " << (apple_present_ ? "Found" : "Not Found") << std::endl;
        return apple_present_ ? BT::NodeStatus::SUCCESS : BT::NodeStatus::FAILURE;
    }
    void setApplePresent(bool present) { apple_present_ = present; }
    static BT::PortsList providedPorts() { return {}; }
private:
    bool apple_present_;
};

// ------------------ Pick Apple ------------------
class PickApple : public BT::SyncActionNode {
public:
    PickApple(const std::string& name, const BT::NodeConfiguration& config)
    : BT::SyncActionNode(name, config) {}
    BT::NodeStatus tick() override {
        std::cout << "Picking the apple" << std::endl;
        return BT::NodeStatus::SUCCESS;
    }
    static BT::PortsList providedPorts() { return {}; }
};

// ------------------ Close Fridge ------------------
class CloseFridgeDoor : public BT::SyncActionNode {
public:
    CloseFridgeDoor(const std::string& name, const BT::NodeConfiguration& config)
    : BT::SyncActionNode(name, config) {}
    BT::NodeStatus tick() override {
        std::cout << "Closing the door of the fridge" << std::endl;
        return BT::NodeStatus::SUCCESS;
    }
    static BT::PortsList providedPorts() { return {}; }
};

// ------------------ Move towards room door ------------------
class MoveTowardsRoomDoor : public BT::SyncActionNode {
public:
    MoveTowardsRoomDoor(const std::string& name, const BT::NodeConfiguration& config)
    : BT::SyncActionNode(name, config) {}
    BT::NodeStatus tick() override {
        std::cout << "Moving towards door of the room" << std::endl;
        return BT::NodeStatus::SUCCESS;
    }
    static BT::PortsList providedPorts() { return {}; }
};

// ------------------ Exit Room ------------------
class ExitRoom : public BT::SyncActionNode {
public:
    ExitRoom(const std::string& name, const BT::NodeConfiguration& config)
    : BT::SyncActionNode(name, config) {}
    BT::NodeStatus tick() override {
        std::cout << "Exiting the room" << std::endl;
        return BT::NodeStatus::SUCCESS;
    }
    static BT::PortsList providedPorts() { return {}; }
};

// ------------------ MAIN ------------------
int main() {
    BT::BehaviorTreeFactory factory;

    factory.registerNodeType<MoveTowardsDoorRoom>("MoveTowardsDoorRoom");
    factory.registerNodeType<CheckRoomDoorClosed>("CheckRoomDoorClosed");
    factory.registerNodeType<OpenDoor>("OpenDoor");
    factory.registerNodeType<EnterRoom>("EnterRoom");
    factory.registerNodeType<MoveTowardsFridgeDoor>("MoveTowardsFridgeDoor");
    factory.registerNodeType<CheckFridgeDoorClosed>("CheckFridgeDoorClosed");
    factory.registerNodeType<FindApple>("FindApple");
    factory.registerNodeType<PickApple>("PickApple");
    factory.registerNodeType<CloseFridgeDoor>("CloseFridgeDoor");
    factory.registerNodeType<MoveTowardsRoomDoor>("MoveTowardsRoomDoor");
    factory.registerNodeType<ExitRoom>("ExitRoom");

    static const char* xml_text = R"(
    <root BTCPP_format="4" main_tree_to_execute="MainTree">
    <BehaviorTree ID="MainTree">
        <Sequence name="root_sequence">
            <MoveTowardsDoorRoom/>
            <Fallback name="door_fallback">
                <Sequence>
                    <CheckRoomDoorClosed/>
                    <OpenDoor/>
                </Sequence>
                <EnterRoom/>
            </Fallback>
            <MoveTowardsFridgeDoor/>
            <Fallback name="fridge_door_fallback">
                <Sequence>
                    <CheckFridgeDoorClosed/>
                    <OpenDoor/>
                </Sequence>
                <FindApple/>
            </Fallback>
            <PickApple/>
            <CloseFridgeDoor/>
            <MoveTowardsRoomDoor/>
            <ExitRoom/>
        </Sequence>
    </BehaviorTree>
</root>
    )";

    auto tree = factory.createTreeFromText(xml_text);

    BT::NodeStatus status = BT::NodeStatus::RUNNING;
    while (status == BT::NodeStatus::RUNNING) {
        status = tree.tickOnce();
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }

    return 0;
}
